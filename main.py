#!/usr/bin/env python3
import sys
import os
import time
from datetime import datetime
import pytz

# Add current directory to path
sys.path.append('.')

from rss_parser import fetch_and_filter_news
from email_notifier import send_email

def main():
    """Main monitoring function"""
    print("🚢 Starting Logistics Monitor")
    print(f"📧 Email: {os.environ.get('LOGISTICS_EMAIL_USER', 'sc.sentinelnews@gmail.com')}")
    print("📊 Monitoring 5 RSS sources for Borouge/ADNOC impact")
    print("-" * 50)
    
    timestamp = datetime.now(pytz.UTC).strftime('[%Y-%m-%d %H:%M:%S.%f]')
    print(f"\n{timestamp} Checking for logistics alerts...")
    
    # Fetch and filter news
    articles = fetch_and_filter_news()
    
    if articles:
        print(f"📧 Sending {len(articles)} critical alerts")
        send_email(articles)
    else:
        print("📭 No critical logistics updates found")
    
    print("✅ Monitoring cycle completed")

if __name__ == "__main__":
    main()
