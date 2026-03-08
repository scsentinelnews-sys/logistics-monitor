import feedparser
import requests
from datetime import datetime, timedelta
import re
from typing import List, Dict, Optional
from config import RSS_SOURCES, BOURUGE_RELEVANCE, MONITORING_CONFIG

class RSSFeedParser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/rss+xml, application/xml, text/xml',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
    
    def fetch_feed(self, source_name: str, source_url: str) -> Optional[List[Dict]]:
        """Fetch and parse RSS feed from a source"""
        try:
            response = self.session.get(source_url, timeout=30)
            response.raise_for_status()
            
            if 'captcha' in response.text.lower() or 'please enable js' in response.text.lower():
                print(f"⚠️ {source_name}: Captcha/JS block detected, trying alternative...")
                response = self.session.get(source_url, params={'format': 'xml'}, timeout=30)
            
            feed = feedparser.parse(response.content)
            articles = []
            
            for entry in feed.entries:
                article = {
                    'title': entry.title,
                    'summary': getattr(entry, 'summary', ''),
                    'content': getattr(entry, 'content', [{}])[0].get('value', '') if hasattr(entry, 'content') else '',
                    'published': getattr(entry, 'published', ''),
                    'link': getattr(entry, 'link', ''),
                    'source': source_name,
                    'category': 'Maritime Logistics'
                }
                articles.append(article)
            
            return articles
            
        except Exception as e:
            print(f"Error fetching feed from {source_name}: {e}")
            return None
    
    def is_within_time_window(self, published_date: str) -> bool:
        """Check if article is within the 6-hour alert window"""
        try:
            date_formats = [
                '%a, %d %b %Y %H:%M:%S %Z',
                '%a, %d %b %Y %H:%M:%S %z',
                '%Y-%m-%dT%H:%M:%SZ',
                '%Y-%m-%dT%H:%M:%S%z'
            ]
            
            parsed_date = None
            for fmt in date_formats:
                try:
                    parsed_date = datetime.strptime(published_date, fmt)
                    if parsed_date.tzinfo is None:
                        parsed_date = parsed_date.replace(tzinfo=datetime.now().astimezone().tzinfo)
                    break
                except ValueError:
                    continue
            
            if parsed_date is None:
                return False
            
            time_diff = datetime.now(parsed_date.tzinfo) - parsed_date
            return time_diff.total_seconds() <= MONITORING_CONFIG['alert_window_hours'] * 3600
            
        except Exception as e:
            print(f"Error parsing date: {e}")
            return False
    
    def passes_keyword_filter(self, article: Dict, source_config: Dict) -> bool:
        """Check if article passes keyword filter"""
        text = f"{article['title']} {article['summary']} {article['content']}".lower()
        
        has_inclusion = any(keyword.lower() in text for keyword in source_config['keywords'])
        has_exclusion = any(exclude.lower() in text for exclude in source_config['exclude'])
        
        return has_inclusion and not has_exclusion
    
    def is_borouge_relevant(self, article: Dict) -> bool:
        """Refined logic: Requires a Stakeholder AND an Operational Impact."""
        text = f"{article['title']} {article['summary']} {article['content']}".lower()
        
        # 1. Instant Discard if it contains Blacklisted words
        if any(word.lower() in text for word in BOURUGE_RELEVANCE['blacklist']):
            return False
        
        # 2. Check for Primary Entities (Who)
        has_entity = any(e.lower() in text for e in BOURUGE_RELEVANCE['entities'])
        
        # 3. Check for Locations (Where)
        has_location = any(l.lower() in text for l in BOURUGE_RELEVANCE['ports_routes'])
        
        # 4. Check for Operational Impact (What)
        has_impact = any(i.lower() in text for i in BOURUGE_RELEVANCE['impact_events'])
        
        # SVP RULE: 
        # An article is relevant ONLY if it mentions (Entity + Impact) OR (Location + Impact)
        is_actionable = (has_entity and has_impact) or (has_location and has_impact)
        
        return is_actionable
    
    def process_article(self, article: Dict, source_config: Dict) -> Optional[Dict]:
        """Process a single article through all filters"""
        # Time window check
        if not self.is_within_time_window(article['published']):
            return None
        
        # Keyword filter check
        if not self.passes_keyword_filter(article, source_config):
            return None
        
        # Borouge relevance check
        if not self.is_borouge_relevant(article):
            return None
        
        # Create operational summary
        summary = self.create_operational_summary(article['content'], article['title'])
        
        return {
            'title': article['title'],
            'summary': summary,
            'source': article['source'],
            'category': article['category'],
            'link': article['link'],
            'published': article['published']
        }
    
    def create_operational_summary(self, content: str, title: str) -> str:
        """Prioritizes sentences containing 'action' triggers (%, days, delays)."""
        action_patterns = [r'\d+%', r'\d+\s*days', r'delay', r'vessel', r'port', r'closed', r'suspended']
        
        sentences = re.split(r'(?<=[.!?])\s+', content)
        action_sentences = []
        
        for sentence in sentences:
            if any(re.search(pattern, sentence.lower()) for pattern in action_patterns):
                action_sentences.append(sentence.strip())
        
        if action_sentences:
            return " | ".join(action_sentences[:2])
        
        return title[:200]
    
    def fetch_all_feeds(self) -> List[Dict]:
        """Fetch and process all RSS feeds"""
        all_articles = []
        
        for source_name, source_url in RSS_SOURCES.items():
            print(f"Fetching from {source_name}...")
            articles = self.fetch_feed(source_name, source_url)
            
            if articles:
                for article in articles:
                    processed = self.process_article(article, 'Maritime Logistics')
                    if processed:
                        all_articles.append(processed)
        
        return all_articles
    
    def fetch_and_filter_news(self) -> List[Dict]:
        """Main function to fetch and filter news"""
        articles = self.fetch_all_feeds()
        
        # Sort by publication date (newest first)
        articles.sort(key=lambda x: x.get('published', ''), reverse=True)
        
        return articles[:EMAIL_CONFIG['max_items']]
