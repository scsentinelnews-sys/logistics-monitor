import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.html import MIMEHTML
from typing import List, Dict
import os
from datetime import datetime

class EmailNotifier:
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        self.sender_email = os.getenv('LOGISTICS_EMAIL_USER')
        self.sender_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
        self.recipient_email = os.getenv('LOGISTICS_EMAIL_RECIPIENT')

    def send_logistics_alert(self, articles: List[Dict]) -> bool:
        """Send logistics alert email with completely clean subject and body"""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = '🚢 Global Logistics Alert'
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            
            # Create COMPLETELY CLEAN HTML content
            html_content = self.create_clean_html_content(articles)
            html_part = MIMEHTML(html_content, 'html')
            
            # Create COMPLETELY CLEAN text content
            text_content = self.create_clean_text_content(articles)
            text_part = MIMEText(text_content, 'plain')
            
            # Attach parts
            msg.attach(text_part)
            msg.attach(html_part)
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

    def create_clean_html_content(self, articles: List[Dict]) -> str:
        """Create clean HTML email content - NO strategic language in body"""
        # Header
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Global Logistics Alert</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                .header {
                    background-color: #f8f9fa;
                    padding: 20px;
                    border-radius: 8px;
                    margin-bottom: 20px;
                    border-left: 4px solid #007bff;
                }
                .article {
                    background-color: #fff;
                    border: 1px solid #e9ecef;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 15px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .article h3 {
                    color: #007bff;
                    margin: 0 0 10px 0;
                    font-size: 16px;
                }
                .article p {
                    margin: 0 0 10px 0;
                    color: #666;
                    font-size: 14px;
                }
                .article .meta {
                    color: #999;
                    font-size: 12px;
                    margin-top: 10px;
                }
                .footer {
                    text-align: center;
                    color: #999;
                    font-size: 12px;
                    margin-top: 30px;
                    padding: 20px;
                    border-top: 1px solid #e9ecef;
                }
                .incident {
                    border-left: 4px solid #dc3545;
                }
                .incident h3 {
                    color: #dc3545;
                }
            </style>
        </head>
        <body>
        """
        
        # Header
        html += """
        <div class="header">
            <h1>🚢 Global Logistics Alert</h1>
            <p><strong>Generated:</strong> """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC') + """</p>
            <p><strong>Articles:</strong> """ + str(len(articles)) + """</p>
        </div>
        """
        
        # Articles - COMPLETELY CLEAN
        for article in articles:
            article_class = 'article'
            if any(keyword in article.get('title', '').lower() or keyword in article.get('summary', '').lower() 
                   for keyword in ['attack', 'explosion', 'fire', 'security breach', 'emergency']):
                article_class += ' incident'
            
            html += f"""
            <div class="{article_class}">
                <h3>{article.get('title', '')}</h3>
                <p>{article.get('summary', '')}</p>
                <div class="meta">Source: {article.get('source', '')} | {article.get('published', '')}</div>
            </div>
            """
        
        # Footer - COMPLETELY CLEAN
        html += """
        <div class="footer">
            <p>📧 Generated by AI Logistics Monitor</p>
            <p>⏰ Next update: Within 30 minutes</p>
        </div>
        </body>
        </html>
        """
        
        return html

    def create_clean_text_content(self, articles: List[Dict]) -> str:
        """Create clean text email content - NO strategic language"""
        text = "🚢 Global Logistics Alert\n"
        text += "=" * 50 + "\n\n"
        text += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
        text += f"Articles: {len(articles)}\n\n"
        
        for i, article in enumerate(articles, 1):
            text += f"{i}. {article.get('title', '')}\n"
            text += f"   {article.get('summary', '')}\n"
            text += f"   Source: {article.get('source', '')} | {article.get('published', '')}\n\n"
        
        text += "=" * 50 + "\n"
        text += "📧 Generated by AI Logistics Monitor\n"
        text += "⏰ Next update: Within 30 minutes\n"
        
        return text

    def send_test_email(self) -> bool:
        """Send test email"""
        test_articles = [
            {
                'title': 'Test Article - Port Congestion Alert',
                'summary': 'This is a test article to verify email delivery.',
                'source': 'Test Source',
                'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
            }
        ]
        
        return self.send_logistics_alert(test_articles)

# Standalone function for compatibility
def send_logistics_alert(articles: List[Dict]) -> bool:
    """Standalone function for sending logistics alerts"""
    notifier = EmailNotifier()
    return notifier.send_logistics_alert(articles)

def send_test_email() -> bool:
    """Standalone function for sending test email"""
    notifier = EmailNotifier()
    return notifier.send_test_email()
