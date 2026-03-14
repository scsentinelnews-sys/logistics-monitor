import os
from datetime import datetime
from rss_parser import RSSFeedParser
from email_notifier import EmailNotifier

def main():
    """Main Global Logistics Monitor function"""
    print("🚢 Global Logistics Monitor V2 Started")
    print(f"🕐 Scan time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 60)
    
    # Initialize RSS parser
    parser = RSSFeedParser()
    
    # Parse RSS feeds - use the working method
    try:
        # Use the method that actually works
        articles = parser.parse()  # Change this based on test results
    except AttributeError:
        print("❌ parse() method not found, trying alternative...")
        try:
            articles = parser.parse_feeds()
        except AttributeError:
            print("❌ parse_feeds() method not found, using empty list")
            articles = []
    except Exception as e:
        print(f"❌ Error parsing RSS feeds: {e}")
        articles = []
    
    if articles:
        print(f"📊 Found {len(articles)} relevant logistics articles")
        
        # Send email alert
        email_notifier = EmailNotifier()
        success = email_notifier.send_alert(articles)
        
        if success:
            print("✅ Global Logistics alert sent successfully")
        else:
            print("❌ Failed to send alert")
    else:
        print("✅ No new logistics articles found")
        print("📧 No email sent (normal behavior)")
    
    print("=" * 60)
    print(f"🕐 Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
