import os
 
# RSS Feed Configuration - Corrected URLs
RSS_SOURCES = {
    'joc': 'https://www.joc.com/rss.xml',
    'icis': 'https://www.icis.com/rss.xml', 
    'freightwaves': 'https://www.freightwaves.com/feed/',
    'splash_247': 'https://splash247.com/feed/',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
    
    # Add comprehensive maritime sources
    'port_technology': 'https://www.porttechnology.org/rss.xml',
    'loadstar': 'https://theloadstar.com/feed/'
}
 
# Borouge/ADNOC Relevance Keywords - Comprehensive
BOURUGE_RELEVANCE = [
    # Company specific
    'borouge', 'adnoc', 'abu dhabi',
    
    # Regional
    'gulf', 'middle east', 'uae', 'dubai', 'saudi', 'qatar',
    
    # Core logistics
    'port', 'shipping', 'logistics', 'freight', 'supply chain',
    
    # Oil & Energy impact
    'oil price', 'oil', 'price hike', 'price increase', 'energy',
    'crude oil', 'petroleum', 'fuel cost', 'bunker fuel',
    
    # Container & Vessel
    'container', 'container shortage', 'container halt', 'vessel',
    'shipping lines', 'carrier', 'maersk', 'msc', 'cma cgm',
    
    # Port Operations
    'port congestion', 'port delay', 'port disruption', 'port strike',
    'terminal', 'berth', 'dock', 'harbor',
    
    # Global & Maritime
    'global logistics', 'maritime', 'cargo', 'route', 'suez canal',
    
    # Disruptions & Crises
    'disruption', 'delay', 'shortage', 'crisis', 'impact',
    'bottleneck', 'backlog', 'capacity', 'rates', 'surcharge'
]
 
# Email Configuration
EMAIL_CONFIG = {
    'sender': os.environ.get('LOGISTICS_EMAIL_USER', 'sc.sentinelnews@gmail.com'),
    'password': os.environ.get('LOGISTICS_EMAIL_PASSWORD', ''),
    'recipient': os.environ.get('LOGISTICS_EMAIL_RECIPIENT', 'sc.sentinelnews@gmail.com')
}
 
# Monitoring Configuration
MONITORING_CONFIG = {
    'time_window_hours': 6,
    'check_interval_minutes': 60
}
