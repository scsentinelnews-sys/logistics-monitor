import os
from email_system import PortIncidentEmail

def test_git_secrets():
    print("🧪 TESTING GITHUB SECRETS INTEGRATION")
    client = PortIncidentEmail()
    
    print(f"🔍 Checking LOGISTICS_EMAIL_USER: {'✅ Found' if client.sender else '❌ MISSING'}")
    print(f"🔍 Checking LOGISTICS_EMAIL_RECIPIENT: {'✅ Found' if client.recipient else '❌ MISSING'}")
    
    if not client.sender or 'your-actual' in client.sender:
        print("❌ FAILED: The system is still seeing placeholders or empty secrets.")
    else:
        print("✅ SUCCESS: System is ready to use GitHub Secrets.")

if __name__ == "__main__":
    test_git_secrets()
