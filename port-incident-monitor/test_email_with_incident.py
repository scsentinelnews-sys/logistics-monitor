import os
from datetime import datetime
from email_system import PortIncidentEmail

def test_email_with_incident():
    """Test email system with mock incident data"""
    print("🧪 TESTING EMAIL WITH MOCK INCIDENT DATA")
    print("=" * 50)
    
    # Check environment variables with new secret names
    email_user = os.getenv('PORT_EMAIL_USER')
    email_password = os.getenv('PORT_EMAIL_PASSWORD')
    email_recipient = os.getenv('PORT_EMAIL_RECIPIENT')
    
    print("🔍 ENVIRONMENT VARIABLES STATUS:")
    print(f"PORT_EMAIL_USER: {'✅ Set' if email_user else '❌ Missing'}")
    print(f"PORT_EMAIL_PASSWORD: {'✅ Set' if email_password else '❌ Missing'}")
    print(f"PORT_EMAIL_RECIPIENT: {'✅ Set' if email_recipient else '❌ Missing'}")
    print("=" * 50)
    
    if not all([email_user, email_password, email_recipient]):
        print("❌ Missing email credentials - cannot test")
        print("🔧 Set environment variables first:")
        print("export PORT_EMAIL_USER='your-gmail@gmail.com'")
        print("export PORT_EMAIL_PASSWORD='your-16-digit-app-password'")
        print("export PORT_EMAIL_RECIPIENT='your-gmail@gmail.com'")
        return False
    
    # Create mock incident data
    mock_incidents = [
        {
            'title': 'TEST: Port Congestion at Khalifa Port - Container Terminal Operations Affected',
            'summary': 'This is a test incident to verify the Port Incident Monitor email system is working correctly. Mock congestion reported at Khalifa Port affecting container terminal operations and vessel scheduling.',
            'source': 'Test System',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'title': 'TEST: Chemical Spill Response at Port Ruwais - Emergency Operations Underway',
            'summary': 'Mock chemical spill incident at Port Ruwais requiring emergency response operations. This is a test to verify email delivery and format for real incidents.',
            'source': 'Test System',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'title': 'TEST: Drone Attack Threat Near Jebel Ali - Security Heightened',
            'summary': 'Mock security incident near Jebel Ali port with drone attack threat. Security operations have been heightened. This is a test to verify the email system works for security incidents.',
            'source': 'Test System',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
    ]
    
    print(f"📧 Sending test email with {len(mock_incidents)} mock incidents...")
    print("📧 Mock incidents:")
    for i, incident in enumerate(mock_incidents, 1):
        print(f"   {i}. {incident['title'][:60]}...")
    
    print("=" * 50)
    
    # Send test email
    try:
        email_client = PortIncidentEmail()
        
        print("📧 Email client created successfully")
        print(f"📧 Recipient: {email_client.recipient}")
        print(f"📧 SMTP Server: {email_client.smtp_server}")
        print(f"📧 SMTP Port: {email_client.smtp_port}")
        print()
        
        result = email_client.send_alert(mock_incidents)
        
        if result:
            print("✅ Test email sent successfully!")
            print("📧 Check your Gmail inbox (including spam folder)")
            print("📧 Subject should be: '🚢 Port Incident Alert - [Date]'")
            print("📧 Email should contain 3 mock incidents in table format")
        else:
            print("❌ Test email failed to send")
            print("🔧 Check Gmail App Password and 2FA settings")
        
        return result
        
    except Exception as e:
        print(f"❌ Error testing email system: {e}")
        print("🔧 Check email configuration and Gmail App Password")
        return False

if __name__ == "__main__":
    success = test_email_with_incident()
    
    print("=" * 50)
    print("🎯 TEST SUMMARY:")
    if success:
        print("✅ Email test: SUCCESS")
        print("✅ Email sending: Working")
        print("✅ Email format: Table format")
        print("✅ Gmail credentials: Correct")
    else:
        print("❌ Email test: FAILED")
        print("❌ Check Gmail App Password")
        print("❌ Check 2-factor authentication")
    
    print("🎯 TEST COMPLETE")
