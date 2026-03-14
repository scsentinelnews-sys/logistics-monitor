import os
import sys
import requests
from datetime import datetime

# 💡 email_system.py is in the SAME directory, not parent
try:
    from email_system import PortIncidentEmail
except ImportError:
    print("❌ CRITICAL: Could not find email_system.py in current directory!")
    sys.exit(1)

def fetch_port_incident_news():
    """Fetch port incident news using NewsAPI"""
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        print("❌ NEWS_API_KEY not found in environment variables")
        return []
    
    # Build search query for port incidents
    query = "port incident OR port disruption OR port congestion OR port security OR port accident"
    
    try:
        url = f"https://newsapi.org/v2/everything"
        params = {
            'q': query,
            'apiKey': api_key,
            'language': 'en',
            'sortBy': 'publishedAt',
            'from': (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)).isoformat(),
            'pageSize': 50
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        articles = data.get('articles', [])
        
        # Filter for relevant port incidents
        relevant_articles = []
        for article in articles:
            title = article.get('title', '').lower()
            description = article.get('description', '').lower()
            
            # Check for GCC port relevance
            gcc_ports = ['khalifa port', 'jebel ali', 'port ruwais', 'abu dhabi port', 'dubai port']
            gcc_materials = ['polyethylene', 'polypropylene', 'polymers', 'crude oil', 'lng', 'chemicals']
            
            is_gcc_port = any(port in title or port in description for port in gcc_ports)
            is_material = any(material in title or material in description for material in gcc_materials)
            
            # Include if it's about GCC ports or materials
            if is_gcc_port or is_material:
                relevant_articles.append({
                    'title': article.get('title', ''),
                    'summary': article.get('description', ''),
                    'source': article.get('source', {}).get('name', 'Unknown'),
                    'published': article.get('publishedAt', '')
                })
        
        print(f"📊 Found {len(relevant_articles)} Port relevant incidents")
        return relevant_articles
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching news: {e}")
        return []
    except Exception as e:
        print(f"❌ Error processing news: {e}")
        return []

def main():
    """Main Port incident monitor function"""
    print("🚨 Port Incident Monitor Started")
    print(f"🕐 Scan time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 60)
    
    # Fetch incident news
    incidents = fetch_port_incident_news()
    
    if incidents:
        print(f"🚨 Found {len(incidents)} Port incidents/updates:")
        for i, incident in enumerate(incidents, 1):
            print(f"   {i}. {incident['title'][:60]}...")
        
        print()
        print("📧 Sending Port incident alert...")
        
        # Send incident alert
        try:
            email_client = PortIncidentEmail()
            success = email_client.send_alert(incidents)
            
            if success:
                print("✅ Port incident alert sent successfully")
            else:
                print("❌ Failed to send incident alert")
        except Exception as e:
            print(f"❌ Error sending email: {e}")
    else:
        print("✅ No new Port incidents detected")
        print("📧 No email sent (normal behavior - no incidents found)")
    
    print("=" * 60)
    print(f"🕐 Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
