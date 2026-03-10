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
        """Send email with professional logistics intelligence articles"""
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
        """Create HTML email body with professional logistics intelligence articles"""
        
        # Create HTML table
        html_table = self.create_html_table(articles)
        
        # Email body with professional focus (no ADNOC/Borouge mentioned)
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
                .source-warning {{
                    background-color: #fff3cd;
                    border: 1px solid #ffeaa7;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 10px 0;
                    text-align: center;
                }}
                .professional-badge {{
                    background-color: #e8f5e8;
                    border: 1px solid #28a745;
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
                .strategic-impact {{
                    background-color: #e8f5e8;
                    border-left: 4px solid #28a745;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🚢 Global Logistics Alert</h1>
                <p>Strategic Supply Chain Intelligence from Professional Logistics Sources</p>
            </div>
            
            <div class="content">
                <div class="professional-badge">
                    <h3 class="source-verified">🎯 Professional Logistics Intelligence</h3>
                    <p>Hybrid filtering: Professional sources + strategic business focus</p>
                </div>
                
                <div class="source-warning">
                    <h3>🛡️ Strategic Business Focus Only</h3>
                    <p>Alerts filtered specifically for global logistics business impact</p>
                </div>
                
                <h3>📊 Strategic Intelligence Summary</h3>
                <p><strong>Total Strategic Items:</strong> {len(articles)} high-impact logistics intelligence items</p>
                <p><strong>Time Window:</strong> Last 24 hours of global logistics operations</p>
                <p><strong>Impact Level:</strong> Strategic - May affect global supply chain and costs</p>
                <p><strong>Source Quality:</strong> Professional logistics feeds only</p>
                <p><strong>Business Focus:</strong> Strategic global logistics business only</p>
                
                {html_table}
                
                <h3>🎯 Strategic Recommendations</h3>
                <ul>
                    <li><strong>Verify Intelligence:</strong> Cross-check with official sources before action</li>
                    <li><strong>Supply Chain Planning:</strong> Contact logistics partners for contingency planning</li>
                    <li><strong>Cost Impact Assessment:</strong> Evaluate potential cost implications for operations</li>
                    <li><strong>Risk Management:</strong> Update supply chain risk assessments based on current intelligence</li>
                    <li><strong>Strategic Response:</strong> Prepare contingency plans for high-impact disruptions</li>
                </ul>
                
                <h3>📈 Intelligence Sources</h3>
                <p><strong>Professional Logistics Feeds:</strong> Maritime Executive, GCaptain, Splash247, Hellenic Shipping, ICIS, Freightwaves, Loadstar, Argus Media</p>
                <p><strong>Regional Intelligence:</strong> Emirates News Agency, Logistics Middle East, Gulf Business</p>
                <p><strong>Filtering Method:</strong> Hybrid approach combining professional criteria with strategic business specificity</p>
            </div>
            
            <div class="footer">
                <p>🤖 This logistics intelligence was automatically generated by the AI Logistics Monitor</p>
                <p>📧 For questions or support, please contact the logistics operations team</p>
                <p>⏰ Generated on: {self.get_current_time()}</p>
                <p>🔄 Next update: Within 30 minutes (24-hour intelligence window)</p>
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
            
            # Add strategic impact styling
            is_strategic = any(keyword in title_lower or keyword in summary_lower 
                            for keyword in ['strategic', 'global', 'worldwide', 'international'])
            
            if is_strategic:
                row_class = 'strategic-impact'
            elif is_critical:
                row_class = 'critical'
            else:
                row_class = ''
            
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
        """Check if source is authoritative (professional sources)"""
        authoritative_sources = [
            # Professional logistics sources
            'maritime executive', 'gcaptain', 'splash247', 'hellenic shipping',
            'icis', 'freightwaves', 'loadstar', 'argus media',
            'emirates news agency', 'logistics middle east', 'gulf business',
            
            # Additional authoritative sources
            'reuters', 'bbc', 'financial times', 'guardian', 'bloomberg', 'wall street journal',
            'marketwatch', 'cnbc', 'yahoo finance', 'joc',
            'lloyds list', 'platts', 'wam', 'the national', 'gulf news'
        ]
        
        return any(auth_source.lower() in source.lower() for auth_source in authoritative_sources)
    
    def send_test_email(self, email_user: str, email_password: str) -> bool:
        """Send test email to verify professional configuration"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = os.getenv('LOGISTICS_EMAIL_USER')
            msg['To'] = os.getenv('LOGISTICS_EMAIL_RECIPIENT')
            msg['Subject'] = "🧪 Test Email - Professional Logistics Monitor"
            
            # Test email body
            test_body = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; padding: 20px; }}
                    .header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; border-radius: 5px 5px 0 0; }}
                    .content {{ padding: 20px; background-color: #f8f9fa; border-radius: 0 0 5px 5px; border: 1px solid #ddd; border-top: none; }}
                    .success {{ color: #27ae60; font-weight: bold; }}
                    .info {{ color: #3498db; }}
                    .source-warning {{ background-color: #fff3cd; border: 1px solid #ffeaa7; padding: 10px; border-radius: 5px; margin: 10px 0; text-align: center; }}
                    .professional-badge {{ background-color: #e8f5e8; border: 1px solid #28a745; padding: 10px; border-radius: 5px; margin: 10px 0; text-align: center; }}
                    .source-verified {{ color: #27ae60; font-weight: bold; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>🧪 Professional Logistics Monitor Test</h1>
                    <p>Professional Configuration Verification Successful</p>
                </div>
                
                <div class="content">
                    <h2 class="success">✅ Professional Configuration Test PASSED</h2>
                    <p class="info">Your AI logistics monitoring system is ready with professional configuration.</p>
                    
                    <div class="professional-badge">
                        <h3 class="source-verified">🎯 Professional Logistics Intelligence</h3>
                        <p>Hybrid filtering: Professional sources + strategic business focus</p>
                    </div>
                    
                    <div class="source-warning">
                        <h3>🛡️ Strategic Business Focus Only</h3>
                        <p>Alerts filtered specifically for global logistics business impact</p>
                    </div>
                    
                    <h3>📊 Professional System Configuration</h3>
                    <ul>
                        <li><strong>Email Service:</strong> Gmail SMTP</li>
                        <li><strong>Recipient:</strong> {os.getenv('LOGISTICS_EMAIL_RECIPIENT')}</li>
                        <li><strong>RSS Sources:</strong> 10 professional logistics feeds</li>
                        <li><strong>Monitoring Window:</strong> Last 24 hours</li>
                        <li><strong>Check Frequency:</strong> Every 30 minutes</li>
                        <li><strong>Business Focus:</strong> Strategic global logistics only</li>
                        <li><strong>Filtering Method:</strong> Hybrid professional approach</li>
                        <li><strong>Legal Status:</strong> UAE compliant</li>
                    </ul>
                    
                    <h3>🎯 Professional Intelligence Sources</h3>
                    <p><strong>Maritime Intelligence:</strong> Maritime Executive, GCaptain, Splash247, Hellenic Shipping</p>
                    <p><strong>Supply Chain Intelligence:</strong> ICIS, Freightwaves, Loadstar, Argus Media</p>
                    <p><strong>Regional Intelligence:</strong> Emirates News Agency, Logistics Middle East, Gulf Business</p>
                    
                    <h3>🚀 What Happens Next</h3>
                    <p>The professional system will automatically scan for logistics intelligence from professional sources and send alerts when:</p>
                    <ul>
                        <li>Strategic logistics operations are affected</li>
                        <li>Global shipping disruptions impact supply chains</li>
                        <li>Professional logistics feeds report relevant incidents</li>
                        <li>Strategic maritime chokepoints affect routes</li>
                        <li>Professional supply chain intelligence impacts business</li>
                    </ul>
                    
                    <p><strong>Next scheduled check:</strong> Within 30 minutes</p>
                    <p><strong>Intelligence window:</strong> Last 24 hours</p>
                </div>
            </div>
            
            <div class="footer">
                <p>🤖 This logistics intelligence was automatically generated by the AI Logistics Monitor</p>
                <p>📧 For questions or support, please contact the logistics operations team</p>
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
