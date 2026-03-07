# RSS Feed Configuration - Simple URL Format
RSS_SOURCES = {
    'cnbc_supply_chain': 'https://www.cnbc.com/id/100727362/device/rss/rss.html',
    'financial_times': 'https://www.ft.com/rss/companies',
    'reuters_business': 'https://www.reuters.com/rssFeed/business',
    'reuters_commodities': 'https://www.reuters.com/rssFeed/commodities',
    'joc': 'https://www.joc.com/rss.xml',
    'freightwaves': 'https://www.freightwaves.com/feed/'
}

# Enhanced Borouge/ADNOC Relevance - Major Carrier Focus
BOURUGE_RELEVANCE = {
    'regions': ['UAE', 'Gulf', 'Middle East', 'Strait of Hormuz', 'Arabian Gulf', 'Persian Gulf', 'Abu Dhabi', 'Dubai', 'Jebel Ali', 'Khalifa', 'Ruweis'],
    'operations': [
        'petrochemical', 'polyethylene', 'propylene', 'chemical tanker', 'specialized shipping', 'LNG', 'gas', 'oil refinery', 
        'container shipping', 'port operations', 'freight forwarding', 'logistics hub', 'terminal operations',
        'container terminal', 'berth', 'dock operations', 'cargo handling', 'vessel operations'
    ],
    'routes': [
        'Gulf-to-Asia', 'Middle East logistics', 'Asia-Middle East', 'UAE shipping', 'Arabian Gulf shipping', 'Strait of Hormuz',
        'container route', 'shipping lane', 'freight corridor', 'logistics route', 'MSC route', 'Maersk route'
    ],
    'ports': [
        'Jebel Ali', 'Abu Dhabi', 'Dubai', 'Khalifa', 'Ruweis', 'Fujairah', 'Khor Fakkan',
        'container terminal', 'port authority', 'shipping hub', 'logistics hub'
    ],
    'companies': [
        'Borouge', 'ADNOC', 'Abu Dhabi National Oil Company', 'ADNOC Gas', 'Borouge Plastics', 'Borouge Polymers',
        # MAJOR CONTAINER LINES - COMPREHENSIVE COVERAGE
        'MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'HMM', 'Yang Ming', 'Zim', 'PIL', 'Hanjin', 'Cosco', 'Wan Hai', 'FOCUS',
        'carrier', 'shipping line', 'container operator', 'vessel operator'
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
    'max_summary_length': 200
}
