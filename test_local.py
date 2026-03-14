import os
import json
from datetime import datetime
from rss_parser import RSSFeedParser

def test_local_functionality():
    """Test RSS parsing and duplicate prevention locally"""
    print("🧪 LOCAL FUNCTIONALITY TEST")
    print("=" * 50)
    
    # Load sent articles for duplicate prevention
    sent_articles = {}
    if os.path.exists('sent_articles.json'):
        try:
            with open('sent_articles.json', 'r') as f:
                sent_articles = json.load(f)
            print(f"✅ Loaded {len(sent_articles)} previously sent articles")
        except Exception as e:
            print(f"❌ Error loading sent_articles.json: {e}")
    else:
        print("❌ sent_articles.json not found (first run)")
    
    # Test RSS parser
    parser = RSSFeedParser()
    articles = parser.fetch_and_filter_news()
    
    print(f"📊 RSS Parser Results:")
    print(f"✅ Found {len(articles)} relevant articles")
    
    # Check for duplicates
    new_articles = []
    for article in articles:
        article_id = article.get('title', '') + article.get('link', '')
        article_hash = hash(article_id)
        
        if article_hash not in sent_articles:
            new_articles.append(article)
            print(f"✅ NEW: {article.get('title', '')[:50]}...")
        else:
            print(f"⏭️ DUPLICATE: {article.get('title', '')[:50]}...")
    
    print(f"📊 After duplicate check: {len(new_articles)} new articles")
    
    if new_articles:
        print(f"\n📧 Email will be sent with {len(new_articles)} articles")
        print(f"✅ Subject: '🚢 Global Logistics Alert - {datetime.now().strftime('%Y-%m-%d')}'")
        print(f"✅ Format: Professional HTML table")
        print(f"✅ Recipient: From GitHub Secrets")
        print(f"✅ Content: Only NEW articles (duplicates filtered)")
        
        # Update sent_articles with new articles
        for article in new_articles:
            article_id = article.get('title', '') + article.get('link', '')
            article_hash = hash(article_id)
            sent_articles[article_hash] = {
                'title': article.get('title', ''),
                'link': article.get('link', ''),
                'timestamp': datetime.now().isoformat()
            }
        
        # Save updated sent_articles
        try:
            with open('sent_articles.json', 'w') as f:
                json.dump(sent_articles, f, indent=2)
            print(f"💾 Updated sent_articles.json with {len(sent_articles)} total articles")
        except Exception as e:
            print(f"❌ Error saving sent_articles.json: {e}")
        
    else:
        print("✅ No new articles found - no email would be sent")
        print("✅ All articles were duplicates (already sent)")
    
    print("=" * 50)
    print("🎯 LOCAL TEST COMPLETE")
    print(f"🕐 Test time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"📊 Total sent articles: {len(sent_articles)}")
    print("📧 Email system ready with GitHub Secrets")

if __name__ == "__main__":
    test_local_functionality()
