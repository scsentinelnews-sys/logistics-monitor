import time
import os
from datetime import datetime
from typing import List, Dict
from rss_parser import RSSFeedParser
from email_notifier import EmailNotifier
from config import MONITORING_CONFIG, EMAIL_CONFIG

class LogisticsMonitor:
    def __init__(self, email_user: str, email_password: str):
        self.parser = RSSFeedParser()
        self.notifier = EmailNotifier()
        self.email_user = email_user
        self.email_password = email_password
        self.last_check_time = None
    
    def check_and_alert(self) -> None:
        """Check for news and send alerts"""
        try:
            print(f"🕐 Starting news check at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Fetch and filter news
            articles = self.parser.fetch_and_filter_news()
            
            if articles:
                print(f"📧 Found {len(articles)} relevant articles, sending alert...")
                
                # Send email alert
                success = self.notifier.send_alert(articles)
                
                if success:
                    print("✅ Email alert sent successfully")
                else:
                    print("❌ Failed to send email alert")
            else:
                print("ℹ️  No relevant articles found")
                
        except Exception as e:
            print(f"❌ Error in check_and_alert: {e}")
    
    def run_continuous(self) -> None:
        """Run continuous monitoring"""
        print("🚀 Starting continuous monitoring...")
        
        while True:
            try:
                self.check_and_alert()
                
                # Wait for next check
                wait_time = MONITORING_CONFIG['check_interval_minutes'] * 60
                print(f"⏰ Next check in {MONITORING_CONFIG['check_interval_minutes']} minutes...")
                time.sleep(wait_time)
                
            except KeyboardInterrupt:
                print("🛑 Monitoring stopped by user")
                break
            except Exception as e:
                print(f"❌ Error in continuous monitoring: {e}")
                time.sleep(60)  # Wait 1 minute before retrying

def main():
    """Main function"""
    print("🌍 Global Logistics Intelligence System")
    print("=" * 50)
    
    # Get email credentials
    email_user = os.getenv('LOGISTICS_EMAIL_USER')
    email_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
    
    if not email_user or not email_password:
        print("❌ Email credentials not found in environment variables")
        print("Please set LOGISTICS_EMAIL_USER and LOGISTICS_EMAIL_PASSWORD")
        return
    
    # Create and run monitor
    monitor = LogisticsMonitor(email_user, email_password)
    
    # Run single check
    monitor.check_and_alert()

if __name__ == "__main__":
    main()
