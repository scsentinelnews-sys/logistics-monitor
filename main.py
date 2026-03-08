import schedule
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
        """Main monitoring function - check feeds and send alerts if needed"""
        print(f"[{datetime.now()}] Starting logistics monitoring check...")
        
        # Fetch and filter articles using the precision targeting method
        articles = self.parser.fetch_and_filter_news()
        
        if articles:
            print(f"Found {len(articles)} actionable intelligence items for operations")
            
            # Send email alert
            success = self.notifier.send_email(articles, self.email_user, self.email_password)
            
            if success:
                print(f"Alert sent successfully with {len(articles)} items")
            else:
                print("Failed to send alert")
        else:
            print("No actionable intelligence found in the last 6 hours")
        
        self.last_check_time = datetime.now()
    
    def run_once(self) -> None:
        """Run monitoring check once (for manual testing)"""
        self.check_and_alert()
    
    def start_monitoring(self) -> None:
        """Start continuous monitoring with scheduled checks"""
        print("🚢 Starting AI Logistics Monitor")
        print(f"📧 Alerts will be sent to: {os.getenv('LOGISTICS_EMAIL_RECIPIENT')}")
        print(f"⏰ Checking every {MONITORING_CONFIG['check_interval_minutes']} minutes")
        print(f"🎯 Alert window: Last {MONITORING_CONFIG['alert_window_hours']} hours")
        print("-" * 50)
        
        # Schedule regular checks
        schedule.every(MONITORING_CONFIG['check_interval_minutes']).minutes.do(self.check_and_alert)
        
        # Run initial check
        self.check_and_alert()
        
        # Keep the scheduler running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute for scheduled tasks
    
    def test_configuration(self) -> bool:
        """Test email configuration and RSS feeds"""
        print("Testing configuration...")
        
        # Test email
        email_success = self.notifier.send_test_email(self.email_user, self.email_password)
        
        if email_success:
            print("✅ Email configuration test passed")
        else:
            print("❌ Email configuration test failed")
            return False
        
        # Test RSS feeds (quick check)
        print("Testing RSS feeds...")
        test_articles = self.parser.fetch_and_filter_news()
        print(f"✅ RSS feeds test completed - found {len(test_articles)} actionable intelligence items")
        
        return True

def main():
    """Main entry point for the logistics monitoring system"""
    
    # Email configuration from environment variables only
    email_user = os.getenv('LOGISTICS_EMAIL_USER')
    email_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
    
    if not email_user or not email_password:
        print("❌ Please configure email credentials in GitHub Secrets:")
        print("  LOGISTICS_EMAIL_USER=your-email@gmail.com")
        print("  LOGISTICS_EMAIL_PASSWORD=your-app-password")
        print("\nNote: For Gmail, use an App Password instead of regular password")
        return
    
    # Initialize monitor
    monitor = LogisticsMonitor(email_user, email_password)
    
    # For GitHub Actions - run production mode directly
    if os.getenv('GITHUB_ACTIONS'):
        print("🤖 Running in GitHub Actions mode - production check")
        monitor.check_and_alert()
        return
    
    # Test configuration
    if not monitor.test_configuration():
        print("❌ Configuration test failed. Please check your settings.")
        return
    
    # Ask user for mode (only for local runs)
    print("\nSelect monitoring mode:")
    print("1. Run once (test)")
    print("2. Start continuous monitoring")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == '1':
            print("Running single check...")
            monitor.run_once()
        elif choice == '2':
            print("Starting continuous monitoring...")
            monitor.start_monitoring()
        else:
            print("Invalid choice. Running single check...")
            monitor.run_once()
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
