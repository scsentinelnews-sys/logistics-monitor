import os
from datetime import datetime
from rss_parser import RSSFeedParser
from email_notifier import EmailNotifier

def main():
    """Main Global Logistics Monitor function"""
    print("🚢 Global Logistics Monitor V2 Started")
    print(f"🕐 Scan time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 60)
    
    # Check environment variables
    email_user = os.getenv('LOGISTICS_EMAIL_USER')
    email_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
    email_recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
    
    print("🔍 ENVIRONMENT VARIABLES:")
    print(f"LOGISTICS_EMAIL_USER: {'✅ Set' if email_user else '❌ Missing'}")
    print(f"LOGISTICS_EMAIL_PASSWORD: {'✅ Set' if email_password else '❌ Missing'}")
    print(f"LOGISTICS_EMAIL_RECIPIENT: {'✅ Set' if email_recipient else '❌ Missing'}")
    print("=" * 60)
    
    # Initialize RSS parser
    parser = RSSFeedParser()
    
    # Parse RSS feeds using the correct method
    try:
        articles = parser.fetch_and_filter_news()
        print(f"📊 RSS parsing completed: Found {len(articles)} relevant articles")
        
        if articles:
            print(f"📋 Latest article: {articles[0].get('title', 'No title')[:50]}...")
            
    except Exception as e:
        print(f"❌ Error parsing RSS feeds: {e}")
        articles = []
    
    if articles:
        print(f"📊 Found {len(articles)} relevant logistics articles")
        
        # Send email alert
        print("📧 Sending email alert...")
        email_notifier = EmailNotifier()
        success = email_notifier.send_alert(articles)
        
        if success:
            print("✅ Global Logistics alert sent successfully")
        else:
            print("❌ Failed to send alert")
    else:
        print("✅ No new logistics articles found")
        print("📧 No email sent (normal behavior - no incidents)")
    
    print("=" * 60)
    print(f"🕐 Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
