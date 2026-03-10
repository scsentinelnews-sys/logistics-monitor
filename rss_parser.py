import feedparser
import requests
from datetime import datetime, timedelta
import re
from typing import List, Dict, Optional
from config import RSS_SOURCES, BOURUGE_RELEVANCE, MONITORING_CONFIG

# Import the tracker
try:
    from sent_articles_tracker import SentArticlesTracker
    TRACKER_AVAILABLE = True
except ImportError:
    TRACKER_AVAILABLE = False
    print("⚠️ SentArticlesTracker not available - duplicate prevention disabled")

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
        
        # Initialize tracker if available
        if TRACKER_AVAILABLE:
            self.tracker = SentArticlesTracker()
        else:
            self.tracker = None
    
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
                    'category': 'Logistics Intelligence'
                }
                articles.append(article)
            
            return articles
            
        except Exception as e:
            print(f"Error fetching feed from {source_name}: {e}")
            return None
    
    def is_within_time_window(self, published_date: str) -> bool:
        """Check if article is within the alert window"""
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
    
    def is_borouge_relevant(self, article: Dict) -> bool:
        """Decision Logic: Target specific logistics impacts"""
        # Use .get() to handle missing keys safely
        text = f"{article.get('title', '')} {article.get('summary', '')} {article.get('content', '')}".lower()
        
        print(f"🔍 Checking article: {article.get('title', 'No title')[:50]}...")
        
        # 1. Instant Discard if it contains Blacklisted words
        blacklist_matches = [word for word in BOURUGE_RELEVANCE['blacklist'] if word.lower() in text]
        if blacklist_matches:
            print(f"❌ BLACKLISTED: {blacklist_matches}")
            return False
        
        # 2. Check for Primary Entities (Who)
        entity_matches = [e for e in BOURUGE_RELEVANCE['entities'] if e.lower() in text]
        has_entity = len(entity_matches) > 0
        print(f"👥 Entities found: {entity_matches}")
        
        # 3. Check for Locations (Where)
        location_matches = [l for l in BOURUGE_RELEVANCE['ports_routes'] if l.lower() in text]
        has_location = len(location_matches) > 0
        print(f"📍 Locations found: {location_matches}")
        
        # 4. Check for Decision Triggers (What)
        impact_matches = [i for i in BOURUGE_RELEVANCE['impact_events'] if i.lower() in text]
        has_impact = len(impact_matches) > 0
        print(f"💥 Impacts found: {impact_matches}")
        
        # DECISION RULE: 
        # Must have BOTH Entity AND Impact OR Location AND Impact
        # This ensures actionable intelligence for decision making
        is_relevant = (has_entity and has_impact) or (has_location and has_impact)
        
        print(f"✅ Relevant: {is_relevant} (Entity+Impact: {has_entity and has_impact}, Location+Impact: {has_location and has_impact})")
        
        return is_relevant
    
    def process_article(self, article: Dict, category: str) -> Optional[Dict]:
        """Process a single article through all filters"""
        # Time window check
        if not self.is_within_time_window(article.get('published', '')):
            return None
        
        # Relevance check
        if not self.is_borouge_relevant(article):
            return None
        
        # Create focused summary
        summary = self.create_summary(article.get('content', ''), article.get('title', ''))
        
        return {
            'title': article.get('title', ''),
            'summary': summary,
            'source': article.get('source', ''),
            'category': category,
            'link': article.get('link', ''),
            'published': article.get('published', '')
        }
    
    def create_summary(self, content: str, title: str) -> str:
        """Create focused summary with specific decision-making facts"""
        # Simple, safe keyword-based summary creation
        summary_parts = []
        
        # Check for financial impact keywords
        financial_keywords = [
            'million', 'billion', 'dollar', 'cost', 'price', 'increase', 'decrease', 
            'surge', 'spike', 'drop', 'loss', 'profit', 'revenue'
        ]
        
        # Check for operational impact keywords
        operational_keywords = [
            'delay', 'disruption', 'congestion', 'closure', 'suspension', 'strike',
            'shortage', 'bottleneck', 'backlog', 'port', 'terminal', 'container'
        ]
        
        # Check for shipping keywords
        shipping_keywords = [
            'maersk', 'msc', 'cma cgm', 'hapag-lloyd', 'one', 'evergreen', 'cosco',
            'vessel', 'ship', 'tanker', 'carrier', 'shipping line'
        ]
        
        # Check for location keywords
        location_keywords = [
            'suez canal', 'strait of hormuz', 'panama canal', 'middle east',
            'khalifa port', 'jebel ali', 'singapore', 'rotterdam', 'shanghai'
        ]
        
        # Extract sentences with key information
        sentences = re.split(r'[.!?]+', content)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 20:
                continue
            
            # Check if sentence contains important keywords
            sentence_lower = sentence.lower()
            has_financial = any(keyword in sentence_lower for keyword in financial_keywords)
            has_operational = any(keyword in sentence_lower for keyword in operational_keywords)
            has_shipping = any(keyword in sentence_lower for keyword in shipping_keywords)
            has_location = any(keyword in sentence_lower for keyword in location_keywords)
            
            # Add sentence if it contains important information
            if (has_financial or has_operational) and (has_shipping or has_location):
                summary_parts.append(sentence)
                if len(summary_parts) >= 2:  # Limit to 2 sentences
                    break
        
        # Create summary
        if summary_parts:
            summary = ' | '.join(summary_parts)
            if len(summary) > MONITORING_CONFIG['max_summary_length']:
                summary = summary[:MONITORING_CONFIG['max_summary_length']] + "..."
        else:
            # Fallback to title with key entities
            summary = title[:MONITORING_CONFIG['max_summary_length']]
        
        return summary
    
    def fetch_all_feeds(self) -> List[Dict]:
        """Fetch and process all RSS feeds"""
        all_articles = []
        
        for source_name, source_url in RSS_SOURCES.items():
            print(f"Fetching from {source_name}...")
            articles = self.fetch_feed(source_name, source_url)
            
            if articles:
                for article in articles:
                    processed = self.process_article(article, 'Logistics Intelligence')
                    if processed:
                        all_articles.append(processed)
        
        # Sort by publication date (most recent first)
        all_articles.sort(key=lambda x: x['published'], reverse=True)
        
        return all_articles
    
    def fetch_and_filter_news(self) -> List[Dict]:
        """Main function to fetch and filter logistics intelligence"""
        print("🚢 Starting logistics intelligence fetch...")
        
        # Fetch all articles and process them directly
        all_articles = self.fetch_all_feeds()
        
        print(f"📊 Found {len(all_articles)} relevant articles")
        
        # Filter out already sent articles if tracker is available
        if self.tracker:
            new_articles = self.tracker.filter_new_articles(all_articles)
            print(f"📧 {len(new_articles)} new articles (duplicates removed)")
            return new_articles
        else:
            print("⚠️ No duplicate prevention available - sending all articles")
            return all_articles

# Standalone function for easy import
def fetch_and_filter_news() -> List[Dict]:
    """Standalone function to fetch and filter logistics intelligence"""
    parser = RSSFeedParser()
    return parser.fetch_and_filter_news()
