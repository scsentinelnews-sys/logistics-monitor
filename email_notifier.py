import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class EmailNotifier:
    def __init__(self):
        self.recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
        self.sender = os.getenv('LOGISTICS_EMAIL_USER')
        self.password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_alert(self, articles):
        if not articles:
            return False

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"🚢 Global Logistics Alert - {datetime.now().strftime('%Y-%m-%d')}"
        msg["From"] = self.sender
        msg["To"] = self.recipient

        # Build Minimalist HTML Body - NO HYPERLINKS
        html_content = self.create_html_content(articles)
        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.recipient, msg.as_string())
            print("✅ Clean email sent successfully.")
            return True
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False

    def create_html_content(self, articles):
        """Create HTML content - NO HYPERLINKS FOR SECURITY"""
        html_content = "<html><body>"
        html_content += "<h2 style='color: #1a365d;'>Latest Logistics Intelligence</h2>"
        html_content += "<hr style='border: 0; border-top: 1px solid #eee;'>"
        
        for article in articles:
            html_content += f"""
            <div style='margin-bottom: 20px; padding: 15px; border: 1px solid #e9ecef; border-radius: 8px; background: white;'>
                <h3 style='margin: 0; color: #2d3748;'>{article['title']}</h3>
                <p style='margin: 5px 0; color: #4a5568;'>{article['summary']}</p>
                <p style='font-size: 12px; color: #a0aec0;'>Source: {article.get('source', '').replace('_', ' ').title()}</p>
            </div>
            """
        
        html_content += "<hr style='border: 0; border-top: 1px solid #eee;'>"
        html_content += f"<p style='font-size: 12px; color: #cbd5e0;'>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} GST</p>"
        html_content += "</body></html>"
        
        return html_content

    def send_test_email(self) -> bool:
        """Send test email"""
        test_articles = [
            {
                'title': 'Test Article - Port Congestion Alert',
                'summary': 'This is a test article to verify email delivery.',
                'source': 'Test Source',
                'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'),
                'link': 'https://example.com/article/1'
            }
        ]
        
        return self.send_alert(test_articles)

# Standalone function for compatibility
def send_logistics_alert(articles):
    """Standalone function for sending logistics alerts"""
    notifier = EmailNotifier()
    return notifier.send_alert(articles)

def send_test_email():
    """Standalone function for sending test email"""
    notifier = EmailNotifier()
    return notifier.send_test_email()
