import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class PortIncidentEmail:
    def __init__(self):
        # SECURE: Pulls directly from GitHub Secrets
        self.sender = os.getenv('LOGISTICS_EMAIL_USER')
        self.password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
        self.recipient = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_alert(self, articles):
        if not articles or not self.sender or not self.password:
            print("❌ Error: Missing credentials or articles.")
            return False

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"🚢 Port Incident Alert - {datetime.now().strftime('%Y-%m-%d')}"
        msg["From"] = self.sender
        msg["To"] = self.recipient

        # Build Clean Table Body
        rows = ""
        for i, a in enumerate(articles, 1):
            rows += f"<tr><td>{i}</td><td>Port Incident</td><td><b>{a['title']}</b><br>{a.get('summary', '')}</td><td>{a['source']}</td></tr>"

        html = f"""
        <html><body>
            <h2>🚨 GCC Port Incident Report</h2>
            <table border="1" cellpadding="10" style="border-collapse: collapse; width: 100%;">
                <tr style="background-color: #f2f2f2;">
                    <th>S.No</th><th>Category</th><th>Details</th><th>Source</th>
                </tr>
                {rows}
            </table>
            <p><small>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC</small></p>
        </body></html>
        """
        
        msg.attach(MIMEText(html, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.recipient, msg.as_string())
            return True
        except Exception as e:
            print(f"❌ SMTP Error: {e}")
            return False

# Global instance for backward compatibility
_port_incident_email = PortIncidentEmail()

def send_port_incident_alert(articles):
    """Send Port incident alert using clean system"""
    return _port_incident_email.send_alert(articles)
