# RSS Feed Configuration - Major Carrier & Vessel Intelligence
RSS_SOURCES = {
    # Current working sources
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
    
    # NEW: Major Carrier Intelligence Sources
    'lloyds_list': {
        'url': 'https://www.lloydslist.com/rssfeed',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'HMM', 'carrier', 'vessel', 'container', 'shipping lines', 'port', 'congestion'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Major Carrier Intelligence'
    },
    'the_loadstar': {
        'url': 'https://theloadstar.com/feed/',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'carrier', 'vessel', 'container', 'shipping lines', 'port', 'congestion'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Freight & Logistics'
    },
    'journal_of_commerce': {
        'url': 'https://www.joc.com/containers/rss.xml',
        'keywords': ['container', 'MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'carrier', 'vessel', 'shipping lines', 'port congestion'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Container Shipping'
    },
    'port_technology': {
        'url': 'https://www.porttechnology.org/rss.xml',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'carrier', 'vessel', 'container', 'port', 'congestion', 'terminal'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Port Operations'
    },
    'american_shipper': {
        'url': 'https://www.americanshipper.com/feed/',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'carrier', 'vessel', 'container', 'shipping lines'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'US Shipping'
    },
    'container_news': {
        'url': 'https://www.container-mag.com/rss.xml',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'carrier', 'vessel', 'container', 'shipping lines', 'port'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Container News'
    },
    
    # Major News Aggregators for Carrier Intelligence
    'reuters_business': {
        'url': 'https://www.reuters.com/business/',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'carrier', 'vessel', 'container', 'shipping lines', 'port congestion'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Global Business'
    },
    'bloomberg_markets': {
        'url': 'https://www.bloomberg.com/markets',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'carrier', 'vessel', 'container', 'shipping lines', 'freight rates'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Market Rates'
    },
    
    # Middle East & Energy Sources
    'arabian_oil_gas': {
        'url': 'https://www.arabianoilandgas.com/rss.xml',
        'keywords': ['UAE', 'Gulf', 'ADNOC', 'Borouge', 'MSC', 'Maersk', 'carrier', 'vessel', 'container'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Middle East Energy'
    },
    'energy_voice': {
        'url': 'https://www.energyvoice.com/feed/',
        'keywords': ['MSC', 'Maersk', 'CMA CGM', 'Hapag-Lloyd', 'carrier', 'vessel', 'container', 'UAE', 'Gulf'],
        'exclude': ['killed', 'dead', 'casualties'],
        'category': 'Energy Logistics'
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
