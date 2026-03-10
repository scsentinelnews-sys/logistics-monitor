import os

# RSS Feed Configuration - Logistics Intelligence
RSS_SOURCES = {
    'cnbc_business': 'https://www.cnbc.com/id/100003114/device/rss/rss.html',
    'bbc_business': 'https://feeds.bbci.co.uk/news/business/rss.xml',
    'financial_times': 'https://www.ft.com/rss/companies',
    'guardian_business': 'https://www.theguardian.com/business/rss',
    'bloomberg_rss': 'https://feeds.bloomberg.com/markets/news.rss',
    'yahoo_finance': 'https://finance.yahoo.com/news/rssindex',
    'marketwatch': 'https://www.marketwatch.com/rss/topstories',
    'joc_container': 'https://www.joc.com/rss.xml',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
    'icis_energy': 'https://www.icis.com/rss/',
    'splash247': 'https://splash247.com/feed/',
    'reuters_commodities': 'https://www.reuters.com/rssFeed/commodities',
}

# Enhanced Logistics Intelligence - Ruwais Abu Dhabi UAE Priority
BOURUGE_RELEVANCE = {
    # Tier 1: Primary Stakeholders (Decision Impact)
    'entities': [
        # ADNOC & Borouge (Highest Priority)
        'ADNOC', 'Borouge', 'Abu Dhabi National Oil Company',
        # Major Container Lines (Direct Impact on Operations)
        'MAERSK', 'MSC', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO', 'HMM', 'Yang Ming', 'Zim', 'PIL',
        # Logistics & Shipping Terms (Direct Impact)
        'shipping', 'container', 'vessel', 'port', 'logistics', 'freight', 'cargo', 'tanker', 'carrier', 'shipping line',
        'supply chain', 'warehouse', 'distribution', 'transport', 'delivery', 'trucking', 'railway',
        # Additional Business Entities (Market Impact)
        'DHL', 'FedEx', 'UPS', 'DB Schenker', 'Kuehne + Nagel', 'Expeditors',
        'Walmart', 'Amazon', 'Target', 'Home Depot', 'IKEA', 'Tesla',
        # Energy & Commodities (Direct Impact)
        'Shell', 'BP', 'ExxonMobil', 'Chevron', 'TotalEnergies',
        'OPEC', 'IEA',
        # UAE Specific Entities
        'Abu Dhabi Ports', 'DP World', 'Etihad Rail', 'Emirates Shipping'
    ],
    
    # Tier 2: Critical Locations (Operations Impact)
    'ports_routes': [
        # Ruwais Abu Dhabi UAE (Highest Priority - Always Catch)
        'Ruwais', 'Ruwais Abu Dhabi', 'Ruwais UAE', 'Ruwais industrial', 'Ruwais refinery', 'Ruwais complex',
        # UAE Critical Locations (Direct Impact)
        'Jebel Ali', 'Khalifa Port', 'Abu Dhabi', 'Dubai', 'Sharjah', 'Fujairah', 'Sohar', 'Mussafah',
        'Mina Jebel Ali', 'Mina Zayed', 'Mina Khalifa',
        # ADNOC/Borouge Specific Locations
        'Borouge plant', 'Borouge complex', 'ADNOC processing', 'ADNOC refinery',
        # Gulf Critical Locations (Direct Impact)
        'Strait of Hormuz', 'Bab el-Mandeb', 'Persian Gulf', 'Gulf of Oman', 'Arabian Gulf',
        # Global Maritime Chokepoints (Supply Chain Impact)
        'Suez Canal', 'Strait of Malacca', 'Panama Canal',
        # Major Global Ports (Operations Impact)
        'Singapore', 'Rotterdam', 'Shanghai', 'Ningbo', 'Hong Kong', 'Busan', 'Los Angeles', 'Long Beach',
        'Hamburg', 'Antwerp', 'New York', 'New Jersey', 'Virginia', 'Savannah', 'Genoa', 'Felixstowe', 'Le Havre', 'Southampton', 'Charleston',
        # Additional Key Locations
        'Middle East', 'Gulf region', 'Red Sea', 'Cape of Good Hope', 'Indian Ocean', 'Mediterranean Sea'
    ],
    
    # Tier 3: Decision Triggers (Specific Impacts - Enhanced)
    'impact_events': [
        # Ruwais Abu Dhabi UAE Attack Priority (Always Catch)
        'fire', 'fire attack', 'attack', 'hit', 'strike', 'assault', 'explosion', 'blast',
        'security breach', 'sabotage', 'incident', 'accident', 'security incident', 'terror attack',
        'emergency', 'crisis', 'damage', 'destruction', 'threat', 'warning', 'alert',
        # Production & Operations Impact (Direct Impact)
        'production halt', 'shutdown', 'suspension', 'operational disruption', 'facility damage',
        'plant closure', 'refinery shutdown', 'processing disruption', 'manufacturing halt',
        # Port Operations (Direct Impact)
        'congestion', 'port congestion', 'port closure', 'port suspension', 'port disruption',
        'port delay', 'port backlog', 'port strike', 'severe disruption', 'yard congestion',
        # Shipping Operations (Schedule Impact)
        'delay', 'delays', 'disruption', 'disruptions', 'blank sailing', 'schedule changes',
        'service suspension', 'route changes', 'capacity constraints', 'total suspension',
        'suspension', 'reroute', 'reroutes', 'detour', 'detours',
        # Safety & Security (Risk Impact)
        'ship attack', 'piracy', 'detention', 'seizure', 'collision', 'grounding',
        'mechanical failure', 'weather disruption', 'security concerns',
        # Market & Cost Impacts (Financial Impact)
        'surcharge', 'rate hike', 'rate increase', 'shortage', 'shortages', 'bottleneck', 'bottlenecks',
        'freight rates', 'rate surge', 'price surge', 'cost increase', '15%', '40%', 'acute',
        # Supply Chain Impacts (Operational Impact)
        'overcapacity', 'underutilization', 'equipment shortage', 'labor shortage', 'customs delay',
        'weather disruption', 'mechanical failure', 'technical issue', 'operational issue',
        'pile up', 'piling up', 'bound containers', 'gulf-bound',
        # Business Impacts (Strategic Impact)
        'profit warning', 'revenue decline', 'margin pressure', 'earnings report',
        'demand surge', 'demand drop', 'capacity issues', 'cost cutting', 'restructuring',
        # Market Impacts (Price Impact)
        'oil price', 'oil prices', 'crude oil', 'natural gas', 'energy prices',
        'polymer prices', 'plastic prices', 'feedstock prices', 'commodity prices',
        'inflation', 'deflation', 'recession', 'market volatility'
    ],
    
    # Tier 4: The "Noise" Filter (Refined - Allow Real UAE Security Content)
    'blacklist': [
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'lifestyle', 'culture', 'tourism', 
        'hospitality', 'real estate', 'entertainment', 'stock market', 'fintech', 'celebrity', 'sports',
        'politics', 'election', 'elections', 'cryptocurrency', 'bitcoin', 'nft', 'gaming', 'fashion',
        'social media', 'venture capital', 'funding', 'investment banking', 'startup', 'personal finance', 'technology'
    ]
}

# Email Configuration - No hardcoded credentials
EMAIL_CONFIG = {
    'recipient': os.getenv('LOGISTICS_EMAIL_RECIPIENT'),
    'sender': os.getenv('LOGISTICS_EMAIL_USER'),
    'subject_prefix': '🚢 Logistics Alert - Impact Analysis',
    'max_items': 5
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 6,
    'max_summary_length': 250
}
