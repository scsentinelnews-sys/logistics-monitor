import os
import sys
from datetime import datetime

# Path to find your email system
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from email_system import PortIncidentEmail

def send_mock_alert():
    print("🚀 FORCING MOCK INCIDENT ALERT...")
    print("🔧 Using GitHub Secrets (no hardcoding)")
    print("=" * 50)
    
    # Check environment variables (GitHub Secrets)
    email_user = os.getenv('LOGISTICS_EMAIL_USER')
    email_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
    email_recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
    
    print("🔍 ENVIRONMENT VARIABLES STATUS:")
    print(f"LOGISTICS_EMAIL_USER: {'✅ Set' if email_user else '❌ Missing'}")
    print(f"LOGISTICS_EMAIL_PASSWORD: {'✅ Set' if email_password else '❌ Missing'}")
    print(f"LOGISTICS_EMAIL_RECIPIENT: {'✅ Set' if email_recipient else '❌ Missing'}")
    print("=" * 50)
    
    if not all([email_user, email_password, email_recipient]):
        print("❌ Missing GitHub Secrets - cannot test")
        print("🔧 Set GitHub Secrets in repository:")
        print("   LOGISTICS_EMAIL_USER: your-gmail@gmail.com")
        print("   LOGISTICS_EMAIL_PASSWORD: your-16-digit-app-password")
        print("   LOGISTICS_EMAIL_RECIPIENT: your-gmail@gmail.com")
        return False
    
    mock_incidents = [
        {
            'title': 'CRITICAL TEST: Simulated Port Congestion at Khalifa Port',
            'summary': 'This is a simulated alert to verify that the Port Incident Monitor email system is working correctly. Mock congestion reported at Khalifa Port affecting container terminal operations and vessel scheduling.',
            'source': 'Test System',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'title': 'CRITICAL TEST: Simulated Chemical Spill at Port Ruwais',
            'summary': 'Mock chemical spill incident at Port Ruwais requiring emergency response operations. This is a test to verify email delivery and format for real incidents.',
            'source': 'Test System',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'title': 'CRITICAL TEST: Simulated Security Threat Near Jebel Ali',
            'summary': 'Mock security incident near Jebel Ali port with security threat. Security operations have been heightened. This is a test to verify the email system works for security incidents.',
            'source': 'Test System',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
    ]
    
    print(f"📧 Sending {len(mock_incidents)} mock incidents...")
    print("📧 Mock incidents:")
    for i, incident in enumerate(mock_incidents, 1):
        print(f"   {i}. {incident['title'][:60]}...")
    print("=" * 50)
    
    try:
        email_client = PortIncidentEmail()
        
        print("📧 Email client created successfully")
        print(f"📧 Recipient: {email_client.recipient}")
        print(f"📧 SMTP Server: {email_client.smtp_server}")
        print(f"📧 SMTP Port: {email_client.smtp_port}")
        print()
        
        result = email_client.send_alert(mock_incidents)
        
        if result:
            print("✅ MOCK INCIDENT ALERT SENT SUCCESSFULLY!")
            print("📧 Check your Gmail inbox (including spam folder)")
            print("📧 Subject: '🚢 Port Incident Alert - [Date]'")
            print("📧 Email should contain 3 mock incidents in table format")
        else:
            print("❌ Could not send email. Check GitHub Secrets.")
        
        return result
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("🔧 Check your GitHub Secrets configuration")
        return False

if __name__ == "__main__":
    print("🧪 FORCE TEST: Mock Incident Alert (GitHub Secrets)")
    print("=" * 60)
    print("🔧 This test uses GitHub Secrets (no hardcoding)")
    print("🔧 Set secrets in GitHub repository settings")
    print("=" * 60)
    
    success = send_mock_alert()
    
    print("=" * 60)
    print("🎯 FORCE TEST COMPLETE")
    if success:
        print("✅ SUCCESS: Email sent using GitHub Secrets")
        print("✅ GitHub Secrets working correctly")
    else:
        print("❌ FAILED: Check GitHub Secrets")
        print("❌ Verify secrets in repository settings")
    print("=" * 60)
