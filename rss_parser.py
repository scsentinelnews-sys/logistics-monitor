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
        """Refined logic: Requires a Stakeholder AND an Operational Impact."""
        text = f"{article['title']} {article['summary']} {article['content']}".lower()
        
        print(f"🔍 Checking article: {article['title'][:50]}...")
        
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
        
        # 4. Check for Operational Impact (What)
        impact_matches = [i for i in BOURUGE_RELEVANCE['impact_events'] if i.lower() in text]
        has_impact = len(impact_matches) > 0
        print(f"💥 Impacts found: {impact_matches}")
        
        # SVP RULE: 
        # An article is relevant ONLY if it mentions (Entity + Impact) OR (Location + Impact)
        is_actionable = (has_entity and has_impact) or (has_location and has_impact)
        
        print(f"✅ Actionable: {is_actionable} (Entity+Impact: {has_entity and has_impact}, Location+Impact: {has_location and has_impact})")
        
        return is_actionable
    
    def process_article(self, article: Dict, category: str) -> Optional[Dict]:
        """Process a single article through all filters"""
        # Time window check
        if not self.is_within_time_window(article['published']):
            return None
        
        # Borouge relevance check
        if not self.is_borouge_relevant(article):
            return None
        
        # Create impactful summary
        summary = self.create_impactful_summary(article['content'], article['title'])
        
        return {
            'title': article['title'],
            'summary': summary,
            'source': article['source'],
            'category': category,
            'link': article['link'],
            'published': article['published']
        }
    
    def create_impactful_summary(self, content: str, title: str) -> str:
        """Create impactful, fact-based summary with specific details"""
        import re
        
        # Priority patterns for impactful content
        impact_patterns = [
            # Specific metrics and numbers
            r'\d+\s*%\s*(increase|decrease|rise|fall|growth|drop)',
            r'\$\d+\s*(million|billion|thousand)',
            r'\d+\s*(days|hours|weeks|months)',
            r'\d+\s*(containers|vessels|ships)',
            r'\d+\s*(percent|%)',
            
            # Specific operational impacts
            r'(port|terminal|facility)\s+(congestion|closure|shutdown|suspension)',
            r'(delay|disruption|disruption|interruption)',
            r'(strike|work stoppage|labor action)',
            r'(capacity|space|equipment)\s+(shortage|constraint|limitation)',
            r'(surcharge|fee|rate)\s+(increase|hike|addition)',
            r'(accident|incident|collision|grounding)',
            r'(weather|storm|typhoon|hurricane)\s+(disruption|damage)',
            r'(customs|inspection|regulation)\s+(delay|backlog|clearance)',
            
            # Company-specific impacts
            r'(MAERSK|MSC|CMA CGM|Hapag-Lloyd|ONE|Evergreen|COSCO)\s+(delay|cancel|suspend)',
            r'(Suez Canal|Strait of Hormuz|Bab el-Mandeb)\s+(block|closure|disruption)',
            r'(container|shipping|freight)\s+(rates|prices|costs)\s+(soar|spike|surge)',
            
            # Time-sensitive operations
            r'(immediate|urgent|critical|emergency)\s+(action|required|needed)',
            r'(effective|starting|beginning)\s+(today|tomorrow|now)',
            r'(expected|estimated|projected)\s+(duration|timeline)',
        ]
        
        # Extract sentences with impact
        sentences = re.split(r'(?<=[.!?])\s+', content)
        impact_sentences = []
        
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 20:  # Skip very short sentences
                continue
                
            # Check for impact patterns
            for pattern in impact_patterns:
                if re.search(pattern, sentence, re.IGNORECASE):
                    # Clean up the sentence
                    cleaned = re.sub(r'\s+', ' ', sentence.strip())
                    cleaned = re.sub(r'\.+$', '', cleaned)
                    
                    # Add to impactful sentences if not duplicate
                    if cleaned not in impact_sentences and len(cleaned) > 20:
                        impact_sentences.append(cleaned)
                    break
        
        # If no impactful sentences found, try to extract key facts from title
        if not impact_sentences:
            title_facts = []
            
            # Look for specific facts in title
            title_patterns = [
                r'(MAERSK|MSC|CMA CGM|Hapag-Lloyd|ONE|Evergreen|COSCO)',
                r'(Suez Canal|Strait of Hormuz|Bab el-Mandeb)',
                r'(Khalifa Port|Jebel Ali|Rotterdam|Singapore|Shanghai)',
                r'\$\d+\s*(million|billion)',
                r'\d+\s*%\s*(increase|decrease)',
                r'\d+\s*(days|hours)\s*(delay|backlog)',
            ]
            
            for pattern in title_patterns:
                match = re.search(pattern, title, re.IGNORECASE)
                if match:
                    title_facts.append(match.group().strip())
            
            if title_facts:
                impact_sentences = title_facts[:2]  # Limit to 2 facts
        
        # Create impactful summary
        if impact_sentences:
            # Take the most impactful sentences
            summary = " | ".join(impact_sentences[:3])  # Limit to 3 sentences
            if len(summary) > MONITORING_CONFIG['max_summary_length']:
                summary = summary[:MONITORING_CONFIG['max_summary_length']] + "..."
        else:
            # Fallback to title with key facts
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
                    processed = self.process_article(article, 'Business News')
                    if processed:
                        all_articles.append(processed)
        
        # Sort by publication date (most recent first)
        all_articles.sort(key=lambda x: x['published'], reverse=True)
        
        return all_articles
    
    def fetch_and_filter_news(self) -> List[Dict]:
        """Main function to fetch and filter all news"""
        all_articles = self.fetch_all_feeds()
        
        # Filter for Borouge/ADNOC relevance
        filtered_articles = []
        for article in all_articles:
            if self.is_borouge_relevant(article):
                filtered_articles.append(article)
        
        return filtered_articles

# Standalone function for easy import
def fetch_and_filter_news() -> List[Dict]:
    """Standalone function to fetch and filter news"""
    parser = RSSFeedParser()
    return parser.fetch_and_filter_news()
