import time
import os
from datetime import datetime
from typing import List, Dict
from rss_parser import RSSFeedParser
from email_system import send_logistics_alert  # Use new clean system
from config import MONITORING_CONFIG

class LogisticsMonitor:
    def __init__(self):
        self.parser = RSSFeedParser()
        self.last_check_time = None
    
    def check_and_alert(self) -> None:
        """Check for news and send alerts if needed"""
        try:
            print(f"[{datetime.now()}] Starting logistics monitoring check...")
            
            # Fetch and filter articles
            articles = self.parser.fetch_and_filter_news()
            
            if articles:
                print(f"Found {len(articles)} actionable intelligence items")
                
                # Send email alert using clean system
                success = send_logistics_alert(articles)
                
                if success:
                    print(f"Alert sent successfully with {len(articles)} items")
                else:
                    print("Failed to send alert")
            else:
                print("No actionable intelligence found")
        
        except Exception as e:
            print(f"❌ Error in check_and_alert: {e}")
    
    def run_once(self) -> None:
        """Run monitoring check once"""
        self.check_and_alert()

def main():
    """Main entry point"""
    print("🌍 Global Logistics Intelligence System")
    print("=" * 50)
    
    # Initialize monitor
    monitor = LogisticsMonitor()
    
    # For GitHub Actions - run production mode directly
    if os.getenv('GITHUB_ACTIONS'):
        print("🤖 Running in GitHub Actions mode - production check")
        monitor.check_and_alert()
        return
    
    # Run single check
    print("Running single check...")
    monitor.run_once()

if __name__ == "__main__":
    main()
