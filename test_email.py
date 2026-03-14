import os
from datetime import datetime
from email_notifier import EmailNotifier

def test_email():
    """Test email system with mock article"""
    print("📧 TESTING EMAIL SYSTEM")
    print("=" * 40)
    
    # Check environment variables
    email_user = os.getenv('LOGISTICS_EMAIL_USER')
    email_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
    email_recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
    
    print("🔍 ENVIRONMENT VARIABLES:")
    print(f"LOGISTICS_EMAIL_USER: {'✅ Set' if email_user else '❌ Missing'}")
    print(f"LOGISTICS_EMAIL_PASSWORD: {'✅ Set' if email_password else '❌ Missing'}")
    print(f"LOGISTICS_EMAIL_RECIPIENT: {'✅ Set' if email_recipient else '❌ Missing'}")
    
    if not all([email_user, email_password, email_recipient]):
        print("❌ Please set all environment variables")
        return False
    
    # Create mock article
    mock_articles = [{
        'title': 'TEST: Lured by Profits, Some Shipowners Brave Mines and Drone Risks in Hormuz',
        'summary': 'This is a test email to verify the Global Logistics Monitor email system is working correctly.',
        'source': 'Test System',
        'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'),
        'category': 'Logistics',
        'link': 'https://test.com'
    }]
    
    print(f"📧 Sending test email with {len(mock_articles)} mock article...")
    
    # Send test email
    try:
        email_notifier = EmailNotifier()
        success = email_notifier.send_alert(mock_articles)
        
        if success:
            print("✅ Test email sent successfully!")
            print("📧 Check your Gmail inbox (including spam folder)")
            print("📧 Subject should be: '🚢 Global Logistics Alert - [Date]'")
        else:
            print("❌ Failed to send test email")
        
        return success
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_email()
