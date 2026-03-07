# RSS Feed Configuration - Fixed Working Sources
RSS_SOURCES = {
    # PROVEN WORKING SOURCES
    'joc': {
        'url': 'https://www.joc.com/rss.xml',
        'keywords': ['container shipping', 'port congestion', 'freight', 'carrier', 'shipping lines', 'MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'vessel', 'container'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Container Shipping'
    },
    'freightwaves': {
        'url': 'https://www.freightwaves.com/feed/',
        'keywords': ['freight', 'shipping', 'logistics', 'supply chain', 'rates', 'capacity', 'container', 'MSC', 'Maersk', 'carrier', 'vessel'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Freight Markets'
    },
    'splash_247': {
        'url': 'https://splash247.com/feed/',
        'keywords': ['shipping', 'maritime', 'vessel', 'port', 'logistics', 'tanker', 'container', 'MSC', 'Maersk', 'carrier', 'shipping lines'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Maritime News'
    },
    'hellenic_shipping': {
        'url': 'https://www.hellenicshippingnews.com/feed/',
        'keywords': ['tanker rates', 'charter rates', 'port delays', 'shipping lines', 'MSC', 'Maersk', 'CMA CGM', 'vessel', 'container'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Shipping Markets'
    },
    'cnbc': {
        'url': 'https://www.cnbc.com/id/100727362/device/rss/rss.html',
        'keywords': ['container', 'shipping', 'logistics', 'freight rates', 'port', 'MSC', 'Maersk', 'carrier', 'vessel'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Supply Chain'
    },
    'financial_times': {
        'url': 'https://www.ft.com/rss/companies',
        'keywords': ['container', 'shipping', 'logistics', 'MSC', 'Maersk', 'carrier', 'vessel'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Business News'
    }
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
        # MAJOR CONTAINER LINES - CRITICAL FOR OPERATIONS
        'MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'HMM', 'Yang Ming', 'Zim', 'PIL',
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
    'check_interval_minutes': 60,
    'alert_window_hours': 6,
    'max_summary_length': 200
}
