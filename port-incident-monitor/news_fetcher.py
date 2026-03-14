import requests
from datetime import datetime, timedelta
from config import NEWS_API_CONFIG, PORT_INCIDENT_TARGETS

class PortIncidentNewsFetcher:
    def __init__(self):
        self.api_key = NEWS_API_CONFIG['api_key']
        self.base_url = NEWS_API_CONFIG['base_url']
        
    def fetch_incident_news(self):
        """Fetch Port specific incident news using NewsAPI"""
        if not self.api_key:
            print("❌ NEWS_API_KEY not found in environment variables")
            return []
        
        # Build query with materials, infrastructure, and exclusions
        materials_query = ' OR '.join([f'"{material}"' for material in PORT_INCIDENT_TARGETS['materials']])
        infrastructure_query = ' OR '.join([f'"{infra}"' for infra in PORT_INCIDENT_TARGETS['infrastructure']])
        exclusions_query = ' '.join([f'-{exclude}' for exclude in PORT_INCIDENT_TARGETS['exclusions']])
        
        # Combined query
        query = f'({materials_query}) AND ({infrastructure_query}) {exclusions_query}'
        
        # Get news from last 6 hours
        from_date = (datetime.now() - timedelta(hours=NEWS_API_CONFIG['time_window_hours'])).strftime('%Y-%m-%dT%H:%M:%S')
        
        # Build URL
        params = {
            'q': query,
            'sortBy': NEWS_API_CONFIG['sort_by'],
            'language': NEWS_API_CONFIG['language'],
            'apiKey': self.api_key,
            'from': from_date,
            'pageSize': NEWS_API_CONFIG['page_size']
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            articles = []
            if data.get('status') == 'ok':
                for item in data.get('articles', [])[:PORT_INCIDENT_TARGETS.get('max_items', 10)]:
                    # Additional filtering to ensure relevance
                    title = item.get('title', '').lower()
                    description = item.get('description', '').lower()
                    content = f"{title} {description}"
                    
                    # Check for Port relevance
                    port_keywords = ['port', 'terminal', 'container', 'shipping', 'maritime', 'congestion', 'disruption', 'delay', 'incident']
                    location_keywords = ['ruwais', 'khalifa port', 'jebel ali', 'dubai', 'abu dhabi', 'uae', 'gcc']
                    
                    has_port = any(keyword in content for keyword in port_keywords)
                    has_location = any(keyword in content for keyword in location_keywords)
                    
                    # Exclude irrelevant content
                    exclude_keywords = [exc.lower() for exc in PORT_INCIDENT_TARGETS['exclusions']]
                    has_exclusions = any(keyword in content for keyword in exclude_keywords)
                    
                    if has_port and has_location and not has_exclusions:
                        articles.append({
                            'title': item.get('title'),
                            'summary': item.get('description') or item.get('content', ''),
                            'source': item.get('source', {}).get('name'),
                            'published': item.get('publishedAt'),
                            'url': item.get('url')
                        })
            
            print(f"📊 Found {len(articles)} Port relevant incidents")
            return articles
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching news: {e}")
            return []
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return []

# Global instance
_news_fetcher = PortIncidentNewsFetcher()

def fetch_port_incident_news():
    """Fetch Port incident news using global instance"""
    return _news_fetcher.fetch_incident_news()
