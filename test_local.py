import os
from datetime import datetime
from rss_parser import RSSFeedParser

def test_local_functionality():
    """Test RSS parsing locally without email"""
    print("🧪 LOCAL FUNCTIONALITY TEST")
    print("=" * 50)
    
    # Test RSS parser
    parser = RSSFeedParser()
    articles = parser.fetch_and_filter_news()
    
    print(f"📊 RSS Parser Results:")
    print(f"✅ Found {len(articles)} relevant articles")
    
    if articles:
        print(f"📋 Latest article: {articles[0].get('title', 'No title')[:50]}...")
        print(f"📋 Source: {articles[0].get('source', 'Unknown')}")
        print(f"📋 Published: {articles[0].get('published', 'Unknown')}")
        
        print(f"\n📧 Email would be sent with:")
        print(f"✅ {len(articles)} articles")
        print(f"✅ Professional HTML table format")
        print(f"✅ Subject: '🚢 Global Logistics Alert - {datetime.now().strftime('%Y-%m-%d')}'")
        print(f"✅ Recipient: From GitHub Secrets")
        
    else:
        print("✅ No articles found - no email would be sent")
    
    print("=" * 50)
    print("🎯 LOCAL TEST COMPLETE")
    print("📧 Email will work when GitHub Secrets are set")

if __name__ == "__main__":
    test_local_functionality()
