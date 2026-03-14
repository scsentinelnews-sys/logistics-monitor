import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append('.')

# Test email configuration
print("🔍 TESTING EMAIL CONFIGURATION")
print('=' * 40)

# Check environment variables
email_user = os.getenv('LOGISTICS_EMAIL_USER')
email_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
email_recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')

print(f"📧 Email User: {'✅ Set' if email_user else '❌ Missing'}")
print(f"🔑 Email Password: {'✅ Set' if email_password else '❌ Missing'}")
print(f"📨 Email Recipient: {'✅ Set' if email_recipient else '❌ Missing'}")

if email_user and email_password and email_recipient:
    print("✅ All email environment variables are set")
    
    # Test email system
    try:
        from email_system import PortIncidentEmail
        
        email_client = PortIncidentEmail()
        
        print("📧 Email client created successfully")
        print(f"📧 Recipient: {email_client.recipient}")
        print(f"📧 Sender: {email_client.sender}")
        print(f"📧 SMTP Server: {email_client.smtp_server}")
        print(f"📧 SMTP Port: {email_client.smtp_port}")
        
        # Create test articles
        test_articles = [
            {
                'title': 'Test Port Incident - System Verification',
                'summary': 'This is a test email to verify the Port Incident Monitor email system is working correctly.',
                'source': 'System Test',
                'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
            }
        ]
        
        print("📧 Sending test email...")
        result = email_client.send_alert(test_articles)
        
        if result:
            print("✅ Test email sent successfully!")
            print("📧 Check your Gmail inbox (including spam folder)")
        else:
            print("❌ Test email failed to send")
            
    except Exception as e:
        print(f"❌ Error testing email system: {e}")
        print("🔧 Check email configuration and Gmail App Password")
else:
    print("❌ Missing email configuration")
    print("🔧 Set environment variables and try again")

print("=" * 40)
print("🎯 EMAIL TEST COMPLETE")
