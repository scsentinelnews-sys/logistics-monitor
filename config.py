# RSS Feed Configuration - Working Maritime Sources
RSS_SOURCES = {
    'freightwaves': 'https://www.freightwaves.com/feed/',
    'reuters_business': 'https://www.reuters.com/rssFeed/business',
    'reuters_commodities': 'https://www.reuters.com/rssFeed/commodities',
    'cnbc_supply_chain': 'https://www.cnbc.com/id/100727362/device/rss/rss.html',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
}

# Precision Targeting - SVP Actionable Intelligence
BOURUGE_RELEVANCE = {
    # Tier 1: Primary Stakeholders (Must mention at least one)
    'entities': [
        'Borouge', 'ADNOC', 'L&S', 'Nimex', 'MAERSK', 'MSC', 'CMA CGM', 
        'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO'
    ],
    # Tier 2: Actionable Locations
    'ports_routes': [
        'Khalifa Port', 'Jebel Ali', 'Ruways', 'Ruwais', 'Suez Canal', 
        'Strait of Hormuz', 'Red Sea', 'Bab el-Mandeb', 'Sohar'
    ],
    # Tier 3: Operational Impact Triggers
    'impact_events': [
        'congestion', 'delay', 'blank sailing', 'force majeure', 'surcharge', 
        'strike', 'closure', 'suspension', 'explosion', 'attack', 'detention'
    ],
    # Tier 4: The "Noise" Filter (Blacklist)
    'blacklist': [
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'lifestyle', 'culture', 'tourism', 
        'hospitality', 'real estate', 'entertainment', 'stock market', 'fintech', 'driving', 'economy', 'economic'
    ]
}

# Email Configuration
EMAIL_CONFIG = {
    'recipient': 'sc.sentinelnews@gmail.com',
    'sender': 'sc.sentinelnews@gmail.com',
    'subject_prefix': 'Logistics Alert - Borouge/ADNOC Impact',
    'max_items': 5
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 6,
    'max_summary_length': 250
}
