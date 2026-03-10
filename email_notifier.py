import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
from typing import List, Dict
from config import EMAIL_CONFIG

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
            msg['From'] = os.getenv('LOGISTICS_EMAIL_USER')
            msg['To'] = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
            msg['Subject'] = EMAIL_CONFIG['subject_prefix']
            
            # Create email body
            email_body = self.create_email_body(articles)
            msg.attach(MIMEText(email_body, 'html'))
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(email_user, email_password)
            text = msg.as_string()
            server.sendmail(os.getenv('LOGISTICS_EMAIL_USER'), os.getenv('LOGISTICS_EMAIL_RECIPIENT'), text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def create_email_body(self, articles: List[Dict]) -> str:
        """Create HTML email body with logistics intelligence articles"""
        
        # Create HTML table
        html_table = self.create_html_table(articles)
        
        # Email body with ADNOC/Borouge global logistics focus
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
                    border-radius: 0 0 5px 5px 0 0;
                    border: 1px solid #ddd;
                    border-top: none;
                }}
                .source-warning {{
                    background-color: #fff3cd;
                    border: 1px solid #ffeaa7;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 10px 0;
                    text-align: center;
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
                .source-verified {{
                    color: #27ae60;
                    font-weight: bold;
                }}
                .critical {{
                    background-color: #fff3cd;
                    border-left: 4px solid #ffc107;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🚢 ADNOC/Borouge Global Logistics Alert</h1>
                <p>Real-time ADNOC/Borouge global logistics intelligence from authoritative sources</p>
            </div>
            
            <div class="content">
                <div class="source-warning">
                    <h3 class="source-verified">🛡️ ADNOC/Borouge Business Focus Only</h3>
                    <p>Alerts filtered specifically for ADNOC/Borouge global logistics business impact</p>
                </div>
                
                <h3>📊 ADNOC/Borouge Logistics Intelligence Summary</h3>
                <p><strong>Total Critical Items:</strong> {len(articles)} global logistics intelligence items detected</p>
                <p><strong>Time Window:</strong> Last 6 hours of global logistics operations</p>
                <p><strong>Impact Level:</strong> High - May affect ADNOC/Borouge global supply chain operations and costs</p>
                <p><strong>Business Focus:</strong> ADNOC/Borouge global logistics business only</p>
                
                {html_table}
                
                <h3>🎯 ADNOC/Borouge RECOMMENDED ACTIONS</h3>
                <ul>
                    <li>Verify all intelligence through official ADNOC/Borouge sources before action</li>
                    <li>Contact ADNOC/Borouge logistics partners for contingency planning</li>
                    <li>Assess potential cost implications for ADNOC/Borouge operations</li>
                    <li>Update ADNOC/Borouge supply chain risk assessments based on current intelligence</li>
                </ul>
            </div>
            
            <div class="footer">
                <p>🤖 This ADNOC/Borouge logistics intelligence was automatically generated by the AI Logistics Monitor</p>
                <p>📧 For questions or support, please contact the ADNOC/Borouge logistics operations team</p>
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
            # Check if source is authoritative
            source = article.get('source', '')
            is_authoritative = self.is_authoritative_source(source)
            
            # Add special styling for critical incidents
            title_lower = article.get('title', '').lower()
            summary_lower = article.get('summary', '').lower()
            
            is_critical = any(keyword in title_lower or keyword in summary_lower 
                           for keyword in ['fire', 'attack', 'explosion', 'security breach', 'emergency'])
            
            row_class = 'critical' if is_critical else ''
            
            source_class = 'source-verified' if is_authoritative else ''
            
            html_table += f"""
                <tr class="{row_class}">
                    <td style="vertical-align: top;">{i}</td>
                    <td style="vertical-align: top;">{article['category']}</td>
                    <td style="vertical-align: top;">
                        <strong>{article['title']}</strong><br>
                        <small>{article['summary']}</small><br>
                        <span class="article-info">Source: {article['source']}</span>
                    </td>
                    <td style="vertical-align: top;">
                        <span class="{source_class}">{article['source'].title()}</span>
                    </td>
                </tr>
            """
        
        html_table += """
            </tbody>
        </table>
        """
        
        return html_table
    
    def is_authoritative_source(self, source: str) -> bool:
        """Check if source is authoritative"""
        authoritative_sources = [
            'reuters', 'bbc', 'financial times', 'guardian', 'bloomberg', 'wall street journal',
            'marketwatch', 'cnbc', 'yahoo finance', 'joc', 'splash247', 'hellenic shipping',
            'lloyds list', 'platts', 'icis', 'argus media',
            'wam', 'the national', 'gulf news'
        ]
        
        return any(auth_source.lower() in source.lower() for auth_source in authoritative_sources)
    
    def send_test_email(self, email_user: str, email_password: str) -> bool:
        """Send test email to verify configuration"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = os.getenv('LOGISTICS_EMAIL_USER')
            msg['To'] = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
            msg['Subject'] = "🧪 Test Email - ADNOC/Borouge Logistics Monitor Configuration"
            
            # Test email body
            test_body = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; padding: 20px; }}
                    .header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; border-radius: 5px 5px 0 0; }}
                    .content {{ padding: 20px; background-color: #f8f9fa; border-radius: 0 0 5px 5px 0 0; border: 1px solid #ddd; border-top: none; }}
                    .success {{ color: #27ae60; font-weight: bold; }}
                    .info {{ color: #3498db; }}
                    .source-warning {{ background-color: #fff3cd; border: 1px solid #ffeaa7; padding: 10px; border-radius: 5px; margin: 10px 0; text-align: center; }}
                    .source-verified {{ color: #27ae60; font-weight: bold; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>🧪 ADNOC/Borouge Logistics Monitor Test</h1>
                    <p>Configuration verification successful</p>
                </div>
                
                <div class="content">
                    <h2 class="success">✅ Email Configuration Test PASSED</h2>
                    <p class="info">Your ADNOC/Borouge AI logistics monitoring system is ready to send operational intelligence alerts.</p>
                    
                    <div class="source-warning">
                        <h3>🛡️ ADNOC/Borouge Business Focus Only</h3>
                        <p>Alerts filtered specifically for ADNOC/Borouge global logistics business impact</p>
                    </div>
                    
                    <h3>📊 System Configuration</h3>
                    <ul>
                        <li><strong>Email Service:</strong> Gmail SMTP</li>
                        <li><strong>Recipient:</strong> {os.getenv('LOGISTICS_EMAIL_RECIPIENT')}</li>
                        <li><strong>RSS Sources:</strong> Authoritative news feeds only</li>
                        <li><strong>Monitoring Window:</strong> Last 6 hours</li>
                        <li><strong>Check Frequency:</strong> Every 30 minutes</li>
                        <li><strong>Business Focus:</strong> ADNOC/Borouge global logistics only</li>
                        <li><strong>Legal Status:</strong> UAE compliant</li>
                    </ul>
                    
                    <h3>🎯 What Happens Next</h3>
                    <p>The system will automatically scan for ADNOC/Borouge logistics intelligence from authoritative sources and send alerts when:</p>
                    <ul>
                        <li>ADNOC/Borouge port operations are affected</li>
                        <li>ADNOC/Borouge shipping delays or route disruptions occur</li>
                        <li>ADNOC/Borouge freight rate spikes impact costs</li>
                        <li>ADNOC/Borouge supply chain disruptions affect deliveries</li>
                        <li>Critical ADNOC/Borouge infrastructure incidents occur</li>
                    </ul>
                    
                    <p><strong>Next scheduled check:</strong> Within 30 minutes</p>
                </div>
            </div>
            
            <div class="footer">
                <p>🤖 This ADNOC/Borouge logistics intelligence was automatically generated by the AI Logistics Monitor</p>
                <p>📧 For questions or support, please contact the ADNOC/Borouge logistics operations team</p>
                <p>⏰ Generated on: {self.get_current_time()}</p>
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
            server.sendmail(os.getenv('LOGISTICS_EMAIL_USER'), os.getenv('LOGISTICS_EMAIL_RECIPIENT'), text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"Error sending test email: {e}")
            return False
    
    def get_current_time(self) -> str:
        """Get current time in readable format"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
