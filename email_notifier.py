import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List, Dict
from config import EMAIL_CONFIG
import os

class EmailNotifier:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.email_user = os.getenv('LOGISTICS_EMAIL_USER')
        self.email_password = os.getenv('LOGISTICS_EMAIL_PASSWORD')
    
    def send_email(self, articles: List[Dict], email_user: str, email_password: str) -> bool:
        """Send email with logistics intelligence articles"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = EMAIL_CONFIG['sender']
            msg['To'] = EMAIL_CONFIG['recipient']
            msg['Subject'] = EMAIL_CONFIG['subject_prefix']
            
            # Create email body
            email_body = self.create_email_body(articles)
            msg.attach(MIMEText(email_body, 'html'))
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(email_user, email_password)
            text = msg.as_string()
            server.sendmail(EMAIL_CONFIG['sender'], EMAIL_CONFIG['recipient'], text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def create_email_body(self, articles: List[Dict]) -> str:
        """Create HTML email body with logistics intelligence articles"""
        
        # Create HTML table
        html_table = self.create_html_table(articles)
        
        # Email body with neutral, professional content
        email_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 1000px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background-color: #2c3e50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 5px 5px 0 0;
                }}
                .content {{
                    background-color: #f8f9fa;
                    padding: 20px;
                    border-radius: 0 0 5px 5px;
                    border: 1px solid #ddd;
                    border-top: none;
                }}
                .footer {{
                    margin-top: 20px;
                    padding: 15px;
                    background-color: #ecf0f1;
                    border-radius: 5px;
                    text-align: center;
                    font-size: 12px;
                    color: #7f8c8d;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                th {{
                    background-color: #34495e;
                    color: white;
                    font-weight: bold;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
                tr:hover {{
                    background-color: #e8f4f8;
                }}
                .article-info {{
                    color: #666;
                    font-style: italic;
                    font-size: 0.9em;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🚢 High-priority operational intelligence for Global Logistics</h1>
                <p>Real-time logistics intelligence requiring attention</p>
            </div>
            
            <div class="content">
                <h3>📊 Logistics Intelligence Summary</h3>
                <p><strong>Total Critical Items:</strong> {len(articles)} actionable intelligence items detected</p>
                <p><strong>Time Window:</strong> Last 6 hours of global logistics operations</p>
                <p><strong>Impact Level:</strong> High - May affect supply chain operations and costs</p>
                
                {html_table}
                
                <h3>🎯 RECOMMENDED ACTIONS</h3>
                <ul>
                    <li>Review all logistics intelligence items for operational impact</li>
                    <li>Contact relevant logistics partners for contingency planning</li>
                    <li>Assess potential cost implications and budget impact</li>
                    <li>Update supply chain risk assessments based on current intelligence</li>
                </ul>
            </div>
            
            <div class="footer">
                <p>🤖 This logistics intelligence was automatically generated by the AI Logistics Monitor</p>
                <p>📧 For questions or support, please contact the logistics operations team</p>
                <p>⏰ Generated on: {self.get_current_time()}</p>
            </div>
        </body>
        </html>
        """
        
        return email_body
    
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
                        <span class="article-info">Source: {article['source']}</span>
                    </td>
                    <td style="vertical-align: top;">{article['source'].title()}</td>
                </tr>
            """
        
        html_table += """
            </tbody>
        </table>
        """
        
        return html_table
    
    def send_test_email(self, email_user: str, email_password: str) -> bool:
        """Send test email to verify configuration"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = EMAIL_CONFIG['sender']
            msg['To'] = EMAIL_CONFIG['recipient']
            msg['Subject'] = "🧪 Test Email - Logistics Monitor Configuration"
            
            # Test email body
            test_body = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; padding: 20px; }}
                    .header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; border-radius: 5px; }}
                    .content {{ padding: 20px; background-color: #f8f9fa; border-radius: 5px; margin-top: 10px; }}
                    .success {{ color: #27ae60; font-weight: bold; }}
                    .info {{ color: #3498db; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>🧪 Logistics Monitor Test</h1>
                    <p>Configuration verification successful</p>
                </div>
                
                <div class="content">
                    <h2 class="success">✅ Email Configuration Test PASSED</h2>
                    <p class="info">Your AI logistics monitoring system is ready to send operational intelligence alerts.</p>
                    
                    <h3>📊 System Configuration</h3>
                    <ul>
                        <li><strong>Email Service:</strong> Gmail SMTP</li>
                        <li><strong>Recipient:</strong> {EMAIL_CONFIG['recipient']}</li>
                        <li><strong>RSS Sources:</strong> 11 logistics and business feeds</li>
                        <li><strong>Monitoring Window:</strong> Last 6 hours</li>
                        <li><strong>Check Frequency:</strong> Every 30 minutes</li>
                    </ul>
                    
                    <h3>🎯 What Happens Next</h3>
                    <p>The system will automatically scan for logistics intelligence and send alerts when:</p>
                    <ul>
                        <li>Port congestion or closures affect operations</li>
                        <li>Shipping delays or route disruptions occur</li>
                        <li>Freight rate spikes impact costs</li>
                        <li>Supply chain disruptions affect deliveries</li>
                    </ul>
                    
                    <p><strong>Next scheduled check:</strong> Within 30 minutes</p>
                </div>
                
                <div style="margin-top: 20px; padding: 15px; background-color: #ecf0f1; border-radius: 5px; text-align: center; font-size: 12px; color: #7f8c8d;">
                    <p>🤖 This is a test email from the AI Logistics Monitor system</p>
                    <p>Generated on: {self.get_current_time()}</p>
                </div>
            </body>
            </html>
            """
            
            msg.attach(MIMEText(test_body, 'html'))
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(email_user, email_password)
            text = msg.as_string()
            server.sendmail(EMAIL_CONFIG['sender'], EMAIL_CONFIG['recipient'], text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"Error sending test email: {e}")
            return False
    
    def get_current_time(self) -> str:
        """Get current time in readable format"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
