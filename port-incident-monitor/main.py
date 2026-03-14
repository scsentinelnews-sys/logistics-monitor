import os
from datetime import datetime
from news_fetcher import fetch_port_incident_news
from email_system import send_port_incident_alert

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
        success = send_port_incident_alert(incidents)
        
        if success:
            print("✅ Port incident alert sent successfully")
        else:
            print("❌ Failed to send incident alert")
    else:
        print("✅ No new Port incidents detected")
    
    print("=" * 60)
    print(f"🕐 Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()
