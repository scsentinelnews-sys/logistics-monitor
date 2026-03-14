import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class EmailNotifier:
    def __init__(self):
        self.sender = os.getenv('LOGISTICS_EMAIL_USER')
        self.password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
        self.recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_alert(self, articles):
        """Send logistics alert with clean HTML table"""
        if not articles or not self.sender or not self.password:
            print("❌ Error: Missing credentials or articles.")
            return False

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"🚢 Global Logistics Alert - {datetime.now().strftime('%Y-%m-%d')}"
        msg["From"] = self.sender
        msg["To"] = self.recipient

        # Build HTML table
        html_content = self.create_html_table(articles)
        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.recipient, msg.as_string())
            return True
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False

    def create_html_table(self, articles):
        """Create clean HTML table for logistics articles"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Global Logistics Alert</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                table { width: 100%; border-collapse: collapse; margin: 20px 0; }
                th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
                th { background-color: #f2f2f2; font-weight: bold; }
                tr:hover { background-color: #f5f5f5; }
                .header { background-color: #e8f4fd; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
                .footer { text-align: center; color: #666; font-size: 12px; margin-top: 30px; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🚢 Global Logistics Alert</h1>
                <p><strong>Generated:</strong> """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC') + """</p>
                <p><strong>Articles:</strong> """ + str(len(articles)) + """</p>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>S.No</th>
                        <th>News Category</th>
                        <th>News Content</th>
                        <th>Source</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        for i, article in enumerate(articles[:10], 1):  # Limit to 10 articles
            html += f"""
                <tr>
                    <td>{i}</td>
                    <td>{article.get('category', 'Logistics')}</td>
                    <td>
                        <strong>{article.get('title', '')}</strong><br>
                        <small>{article.get('summary', '')}</small>
                    </td>
                    <td>{article.get('source', '').title()}</td>
                </tr>
            """
        
        html += """
                </tbody>
            </table>
            
            <div class="footer">
                <p>Generated on: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC') + """</p>
                <p>Global Logistics Monitor V2 - Every 30 minutes</p>
            </div>
        </body>
        </html>
        """
        
        return html
