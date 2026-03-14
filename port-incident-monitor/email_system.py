import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class PortIncidentEmail:
    def __init__(self):
        self.recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
        self.sender = os.getenv('LOGISTICS_EMAIL_USER')
        self.password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_alert(self, articles):
        """Send Port incident alert with table only"""
        if not articles:
            return False

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"🚢 Port Incident Alert - {datetime.now().strftime('%Y-%m-%d')}"
        msg["From"] = self.sender
        msg["To"] = self.recipient

        # Build HTML table only - NO STRATEGIC LANGUAGE
        html_content = self.create_table_only(articles)
        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.recipient, msg.as_string())
            print("✅ Port incident email sent successfully.")
            return True
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False

    def create_table_only(self, articles):
        """Create HTML table only - NO STRATEGIC LANGUAGE"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Port Incident Alert</title>
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
                    border-left: 4px solid #dc3545;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }
                th, td {
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }
                th {
                    background-color: #f8f9fa;
                    font-weight: bold;
                    color: #495057;
                }
                tr:hover {
                    background-color: #f8f9fa;
                }
                .footer {
                    text-align: center;
                    color: #6c757d;
                    font-size: 12px;
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #dee2e6;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🚢 Port Incident Alert</h1>
                <p><strong>Generated:</strong> """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC') + """</p>
                <p><strong>Articles:</strong> """ + str(len(articles)) + """</p>
                <p><strong>Focus:</strong> Polyethylene, Polypropylene, Polymers, Crude Oil, LNG, Chemicals</p>
                <p><strong>Infrastructure:</strong> Port Ruwais, Khalifa Port, Jebel Ali, L&S Fleet</p>
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
        
        for i, article in enumerate(articles, 1):
            html += f"""
                <tr>
                    <td>{i}</td>
                    <td>Port Incident</td>
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
                <p>Port Incident Monitor - Every 30 minutes</p>
            </div>
        </body>
        </html>
        """
        
        return html

# Global instance
_port_incident_email = PortIncidentEmail()

def send_port_incident_alert(articles):
    """Send Port incident alert using clean system"""
    return _port_incident_email.send_alert(articles)
