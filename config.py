# RSS Feed Configuration - Working Open Access Sources
RSS_SOURCES = {
    # Tier 1: Major Business & News (Working Sources)
    'cnbc_business': 'https://www.cnbc.com/id/100003114/device/rss/rss.html',
    'bbc_business': 'https://feeds.bbci.co.uk/news/business/rss.xml',
    'financial_times': 'https://www.ft.com/rss/companies',
    'guardian_business': 'https://www.theguardian.com/business/rss',
    'wall_street_journal': 'https://feeds.wsj.com/rss/world_news',
    
    # Tier 2: Available Maritime Sources
    'joc_container': 'https://www.joc.com/rss.xml',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
    'icis_energy': 'https://www.icis.com/rss/',
    'splash247': 'https://splash247.com/feed/',
    
    # Tier 3: Alternative Business Sources
    'bloomberg_business': 'https://www.bloomberg.com/feed/business',
    'reuters_alternative': 'https://feeds.reuters.com/news/wealth',
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
