# RSS Feed Configuration - Comprehensive Global Logistics Coverage
RSS_SOURCES = {
    # Tier 1: Major Business & News (High Access)
    'reuters_business': 'https://www.reuters.com/rssFeed/business',
    'reuters_commodities': 'https://www.reuters.com/rssFeed/commodities',
    'cnbc_business': 'https://www.cnbc.com/id/100003114/device/rss/rss.html',
    'bbc_business': 'https://feeds.bbci.co.uk/news/business/rss.xml',
    'financial_times': 'https://www.ft.com/rss/companies',
    
    # Tier 2: Specialized Maritime Logistics (Try Multiple URLs)
    'joc_container': 'https://www.joc.com/rss.xml',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
    'freightwaves': 'https://www.freightwaves.com/feed/',
    'splash247': 'https://splash247.com/feed/',
    'lloyds_list': 'https://www.lloydslist.com/rssfeed',
    
    # Tier 3: Energy & Petrochemical (Borouge/ADNOC Focus)
    'argus_energy': 'https://www.argusmedia.com/rss',
    'icis_energy': 'https://www.icis.com/rss/',
    'energy_voice': 'https://www.energyvoice.com/feed/',
    'arabian_oil_gas': 'https://www.arabianoilandgas.com/rss.xml',
}

# Precision Targeting - Enhanced Borouge/ADNOC Global Logistics Intelligence
BOURUGE_RELEVANCE = {
    # Tier 1: Primary Stakeholders (Must mention at least one)
    'entities': [
        # Borouge/ADNOC Specific
        'Borouge', 'ADNOC', 'Abu Dhabi National Oil Company', 'ADNOC Gas', 'Borouge Plastics', 'Borouge Polymers', 'L&S', 'Nimex',
        # Major Container Lines (Comprehensive)
        'MAERSK', 'MSC', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO', 'HMM', 'Yang Ming', 'Zim', 'PIL',
        # Logistics & Shipping Terms
        'shipping', 'container', 'vessel', 'port', 'logistics', 'freight', 'cargo', 'tanker', 'carrier', 'shipping line'
    ],
    
    # Tier 2: Actionable Locations (Global + Regional Focus)
    'ports_routes': [
        # UAE/Gulf Critical Locations
        'Khalifa Port', 'Jebel Ali', 'Abu Dhabi', 'Dubai', 'Ruways', 'Ruwais', 'Fujairah', 'Sohar',
        # Global Maritime Chokepoints
        'Suez Canal', 'Strait of Hormuz', 'Bab el-Mandeb', 'Strait of Malacca', 'Panama Canal',
        # Major Global Ports
        'Singapore', 'Rotterdam', 'Shanghai', 'Ningbo', 'Hong Kong', 'Busan', 'Los Angeles', 'Long Beach',
        'Hamburg', 'Antwerp', 'New York', 'New Jersey', 'Virginia', 'Savannah'
    ],
    
    # Tier 3: Operational Impact Triggers (Comprehensive)
    'impact_events': [
        # Disruptions & Delays
        'congestion', 'delay', 'delays', 'disruption', 'disruptions', 'blank sailing', 'force majeure',
        # Operational Issues
        'strike', 'closure', 'closures', 'suspension', 'suspensions', 'shutdown', 'shutdowns',
        # Safety & Security
        'attack', 'attacks', 'detention', 'detentions', 'piracy', 'incident', 'accident',
        # Market & Cost Impacts
        'surcharge', 'rate hike', 'rate increase', 'shortage', 'shortages', 'bottleneck', 'bottlenecks'
    ],
    
    # Tier 4: The "Noise" Filter (Enhanced Blacklist)
    'blacklist': [
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'lifestyle', 'culture', 'tourism', 
        'hospitality', 'real estate', 'entertainment', 'stock market', 'fintech', 'driving', 'economy', 'economic',
        'sports', 'celebrity', 'politics', 'election', 'elections', 'cryptocurrency', 'bitcoin', 'nft'
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
