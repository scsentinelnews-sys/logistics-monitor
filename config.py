import os

# RSS Feed Configuration - Comprehensive High-Alert Coverage
RSS_SOURCES = {
    # Logistics specialized sources
    'joc': 'https://www.joc.com/rss.xml',
    'icis': 'https://www.icis.com/rss.xml', 
    'freightwaves': 'https://www.freightwaves.com/feed/',
    'splash_247': 'https://splash247.com/feed/',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
    
    # Major news aggregators - HIGH ALERT
    'google_news_business': 'https://news.google.com/rss/topics/CAAqJQgKIhNDQklTRERFZWFnM2NlYmRjZmMwYjE0ZThhYjY4ZDc5ZDcxMWI1YjE5ZTc?hl=en-US&gl=US&ceid=US%3Aen',
    'yahoo_business': 'https://www.yahoo.com/news/rss/business',
    'cnbc': 'https://www.cnbc.com/id/100727362/device/rss/rss.html',
    'financial_times': 'https://www.ft.com/rss/companies'
}

# High-Alert Keywords for Critical Incidents
BOURUGE_RELEVANCE = [
    # Company specific
    'borouge', 'adnoc', 'abu dhabi',
    
    # Regional hotspots
    'gulf', 'middle east', 'uae', 'dubai', 'saudi', 'qatar', 'suez canal', 'red sea',
    
    # CRITICAL MARITIME INCIDENTS
    'container ship', 'ship hit', 'collision', 'grounding', 'stranded', 'sinking',
    'red sea', 'houthi', 'missile', 'attack', 'security', 'piracy', 'hijack',
    
    # CRITICAL INFRASTRUCTURE
    'port strike', 'port closure', 'port blocked', 'canal blocked', 'suez canal',
    'supply chain disruption', 'shipping crisis', 'logistics crisis', 'emergency',
    
    # Oil & Energy Impact
    'oil price', 'oil', 'price hike', 'price increase', 'energy', 'crude oil',
    'petroleum', 'fuel cost', 'bunker fuel', 'opec', 'energy crisis',
    
    # Container & Vessel Operations
    'container', 'container shortage', 'container halt', 'vessel', 'shipping lines',
    'carrier', 'maersk', 'msc', 'cma cgm', 'hapag-lloyd', 'evergreen',
    
    # Port Operations
    'port congestion', 'port delay', 'port disruption', 'terminal', 'berth',
    'dock', 'harbor', 'logistics hub', 'port authority',
    
    # Global Trade Impact
    'global logistics', 'maritime', 'cargo', 'route', 'trade', 'tariff',
    'sanctions', 'embargo', 'trade war', 'supply chain', 'import', 'export',
    
    # Market & Financial Impact
    'rates', 'surcharge', 'freight rates', 'shipping costs', 'inflation',
    'disruption', 'delay', 'shortage', 'crisis', 'impact', 'emergency', 'critical'
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
