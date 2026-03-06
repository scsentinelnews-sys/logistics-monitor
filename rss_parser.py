import feedparser
import requests
from datetime import datetime, timedelta
import pytz
from config import RSS_SOURCES, BOURUGE_RELEVANCE, MONITORING_CONFIG

def fetch_and_filter_news():
    """Fetch and filter RSS news for Borouge/ADNOC relevance"""
    articles = []
    time_threshold = datetime.now(pytz.UTC) - timedelta(hours=MONITORING_CONFIG['time_window_hours'])
    
    for source_name, url in RSS_SOURCES.items():
        print(f"Fetching from {source_name}...")
        try:
            # Fetch RSS feed
            response = requests.get(url, timeout=10)
            feed = feedparser.parse(response.content)
            
            for entry in feed.entries:
                # Parse publication date
                pub_date = entry.get('published_parsed')
                if pub_date:
                    pub_datetime = datetime(*pub_date[:6], tzinfo=pytz.UTC)
                    
                    # Check if within time window
                    if pub_datetime > time_threshold:
                        # Check Borouge relevance
                        title = entry.title.lower()
                        summary = entry.summary.lower() if hasattr(entry, 'summary') else ''
                        
                        # Check for relevant keywords
                        if any(keyword in title or keyword in summary for keyword in BOURUGE_RELEVANCE):
                            articles.append({
                                'title': entry.title,
                                'summary': entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary,
                                'published': pub_datetime,
                                'source': source_name,
                                'category': 'Logistics Alert'
                            })
        
        except Exception as e:
            print(f"❌ Error fetching {source_name}: {e}")
    
    return articles
