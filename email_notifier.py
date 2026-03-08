import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
from typing import List, Dict
from config import EMAIL_CONFIG, MONITORING_CONFIG

class EmailNotifier:
    def __init__(self, smtp_server: str = 'smtp.gmail.com', smtp_port: int = 587):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def create_html_table(self, articles: List[Dict]) -> str:
        """Create HTML table with 4 columns as specified"""
        html_table = """
        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
            <thead style="background-color: #f2f2f2; font-weight: bold;">
                <tr>
                    <th style="text-align: left; width: 5%;">S.no</th>
                    <th style="text-align: left; width: 20%;">News Category</th>
                    <th style="text-align: left; width: 55%;">News Content</th>
                    <th style="text-align: left; width: 20%;">Source</th>
                </tr>
            </thead>
            <tbody>
        """
        
        for i, article in enumerate(articles[:EMAIL_CONFIG['max_items']], 1):
            html_table += f"""
                <tr>
                    <td style="vertical-align: top;">{i}</td>
                    <td style="vertical-align: top;">{article['category']}</td>
                    <td style="vertical-align: top;">
                        <strong>{article['title']}</strong><br>
                        <small>{article['summary']}</small><br>
                        <a href="{article['link']}" style="color: #0066cc; text-decoration: none;">Read more</a>
                    </td>
                    <td style="vertical-align: top;">{article['source'].title()}</td>
                </tr>
            """
        
        html_table += """
            </tbody>
        </table>
        """
        
        return html_table
    
    def create_email_body(self, articles: List[Dict]) -> str:
        """Create HTML email body with operational intelligence"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        
        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                .header {{ background-color: #1f497d; color: white; padding: 20px; text-align: center; }}
                .content {{ margin: 20px 0; }}
                .footer {{ background-color: #f2f2f2; padding: 15px; font-size: 12px; color: #666; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h2>🚢 Logistics Alert - Borouge/ADNOC Impact Analysis</h2>
                <p>High-priority operational intelligence for Global Logistics SVP</p>
            </div>
            
            <div class="content">
                <h3>📊 Critical Logistics Updates (Last {MONITORING_CONFIG['alert_window_hours']} Hours)</h3>
                <p><strong>Total Items:</strong> {len(articles)} | <strong>Generated:</strong> {timestamp}</p>
                
                {self.create_html_table(articles)}
                
                <h3>🎯 Operational Impact Summary</h3>
                <p>This alert contains news items that may impact Borouge/ADNOC logistics operations including:</p>
                <ul>
                    <li>Shipping route disruptions in Gulf/Middle East region</li>
                    <li>Port congestion affecting petrochemical shipments</li>
                    <li>Freight rate changes impacting supply chain costs</li>
                    <li>Vessel operational issues affecting delivery schedules</li>
                </ul>
                
                <p><strong>Recommended Actions:</strong></p>
                <ul>
                    <li>Review vessel schedules for potential delays</li>
                    <li>Contact logistics partners for alternate routing options</li>
                    <li>Monitor port status for operational continuity</li>
                </ul>
            </div>
            
            <div class="footer">
                <p>📧 AI Logistics Monitor | Automated Operational Intelligence System</p>
                <p>For immediate operational decisions, verify critical information through official channels</p>
            </div>
        </body>
        </html>
        """
        
        return html_body
    
    def send_email(self, articles: List[Dict], sender_email: str, sender_password: str) -> bool:
        """Send email notification with logistics alerts"""
        if not articles:
            print("No articles to send")
            return False
        
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f'🚢 Logistics Alert - {len(articles)} Critical Updates Found'
            msg['From'] = sender_email
            msg['To'] = EMAIL_CONFIG['recipient']
            
            html_body = self.create_email_body(articles)
            msg.attach(MIMEText(html_body, 'html'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
            
            print(f"📧 Email sent successfully to {EMAIL_CONFIG['recipient']}")
            return True
            
        except Exception as e:
            print(f"❌ Email failed: {e}")
            return False
    
    def send_test_email(self, sender_email: str, sender_password: str) -> bool:
        """Send test email to verify system is working"""
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = "✅ Logistics Monitor Test Successful"
            msg["From"] = sender_email
            msg["To"] = EMAIL_CONFIG["recipient"]
            
            body = f"""
            <html>
            <body>
                <h2>✅ Logistics Monitor Test Successful</h2>
                <p>Your AI logistics monitoring system is now active and configured.</p>
                <p>You will receive alerts when actionable logistics intelligence affecting Borouge/ADNOC operations is detected.</p>
                <br>
                <p><strong>System Status:</strong> Active</p>
                <p><strong>Monitoring Sources:</strong> 11 optimized RSS sources (CNBC, BBC, FT, Guardian, Bloomberg, Yahoo Finance, MarketWatch, JOC, Hellenic, ICIS, Splash247)</p>
                <p><strong>Alert Window:</strong> Last {MONITORING_CONFIG["alert_window_hours"]} hours</p>
            </body>
            </html>
            """
            
            msg.attach(MIMEText(body, "html"))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, EMAIL_CONFIG["recipient"], msg.as_string())
            server.quit()
            
            print(f"📧 Test email sent successfully to {EMAIL_CONFIG["recipient"]}")
            return True
            
        except Exception as e:
            print(f"❌ Test email failed: {e}")
            return False
            
        except Exception as e:
            print(f"❌ Test email failed: {e}")
            return False
