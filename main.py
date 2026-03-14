import os
import json
from datetime import datetime, timedelta
from rss_parser import RSSFeedParser
from email_notifier import EmailNotifier

def load_sent_articles():
    """Load sent articles from JSON file"""
    try:
        if os.path.exists('sent_articles.json'):
            with open('sent_articles.json', 'r') as f:
                data = json.load(f)
                print(f"✅ Loaded {len(data)} sent articles")
                return data
    except Exception as e:
        print(f"❌ Error loading sent_articles.json: {e}")
        return {}

def save_sent_articles(sent_articles):
    """Save sent articles to JSON file"""
    try:
        with open('sent_articles.json', 'w') as f:
            json.dump(sent_articles, f, indent=2)
        print(f"💾 Saved {len(sent_articles)} sent articles")
    except Exception as e:
        print(f"❌ Error saving sent_articles: {e}")

def main():
    """Main Global Logistics Monitor function"""
    print("🚢 Global Logistics Monitor V2 Started")
    print(f"🕐 Scan time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 60)
    
    # Load sent articles for duplicate prevention
    sent_articles = load_sent_articles()
    print(f"🔍 Loaded {len(sent_articles)} previously sent articles")
    
    # Initialize RSS parser
    parser = RSSFeedParser()
    
    # Parse RSS feeds
    articles = parser.fetch_and_filter_news()
    print(f"📊 Found {len(articles)} relevant logistics articles")
    
    # Filter out duplicates using a longer time window
    new_articles = []
    for article in articles:
        article_id = article.get('title', '') + article.get('link', '')
        article_hash = hash(article_id)
        
        # Check if article was sent in the last 24 hours
        if article_hash in sent_articles:
            try:
                timestamp_str = sent_articles[article_hash].get('timestamp', '')
                if timestamp_str:
                    sent_time = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                    time_diff = datetime.now() - sent_time
                    if time_diff.total_seconds() < 86400:  # 24 hours
                        print(f"⏭️ Skipping recent duplicate: {article.get('title', '')[:50]}...")
                        continue
            except Exception as e:
                print(f"❌ Error checking timestamp: {e}")
        
        # Article is new or older than 24 hours
        new_articles.append(article)
        sent_articles[article_hash] = {
            'title': article.get('title', ''),
            'link': article.get('link', ''),
            'timestamp': datetime.now().isoformat()
        }
    
    print(f"📊 After duplicate check: {len(new_articles)} new articles")
    
    if new_articles:
        print(f"📊 Found {len(new_articles)} NEW logistics articles")
        
        # Send email alert
        print("📧 Sending email alert...")
        email_notifier = EmailNotifier()
        success = email_notifier.send_alert(new_articles)
        
        if success:
            print("✅ Global Logistics alert sent successfully")
            # Save updated sent articles
            save_sent_articles(sent_articles)
        else:
            print("❌ Failed to send alert")
    else:
        print("✅ No new logistics articles found")
        print("📧 No email sent (normal behavior - no new incidents)")
    
    print("=" * 60)
    print(f"🕐 Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
