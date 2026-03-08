# RSS Feed Configuration - SVP-Focused Logistics Intelligence
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
    'argus_media': 'https://www.argusmedia.com/rss/',
    'platts': 'https://www.platts.com/rss/',
    'oilprice': 'https://oilprice.net/feed/',
    'freightwaves': 'https://www.freightwaves.com/feed/',
}

# SVP-Focused Logistics Intelligence - Targeted for Decision Making
BOURUGE_RELEVANCE = {
    # Tier 1: Primary Stakeholders (SVP Decision Impact)
    'entities': [
        # Borouge/ADNOC Specific (Direct Impact)
        'Borouge', 'ADNOC', 'Abu Dhabi National Oil Company', 'ADNOC Gas', 'Borouge Plastics', 'Borouge Polymers', 'L&S', 'Nimex',
        # Major Container Lines (Direct Impact on Operations)
        'MAERSK', 'MSC', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO', 'HMM', 'Yang Ming', 'Zim', 'PIL',
        # Logistics Giants (Market Impact)
        'DHL', 'FedEx', 'UPS', 'DB Schenker', 'Kuehne + Nagel', 'Expeditors',
        # Major Retailers (Supply Chain Impact)
        'Walmart', 'Amazon', 'Target', 'Home Depot', 'IKEA', 'Tesla',
        # Energy & Commodities (Direct Impact)
        'Shell', 'BP', 'ExxonMobil', 'Chevron', 'TotalEnergies',
        'OPEC', 'IEA'
    ],
    
    # Tier 2: Critical Locations (Operations Impact)
    'ports_routes': [
        # UAE/Gulf Critical Locations (Direct Borouge Impact)
        'Khalifa Port', 'Jebel Ali', 'Ruways', 'Ruwais', 'Fujairah', 'Sohar',
        # Global Maritime Chokepoints (Supply Chain Impact)
        'Suez Canal', 'Strait of Hormuz', 'Bab el-Mandeb', 'Strait of Malacca', 'Panama Canal',
        # Major Global Ports (Operations Impact)
        'Singapore', 'Rotterdam', 'Shanghai', 'Ningbo', 'Hong Kong', 'Busan', 'Los Angeles', 'Long Beach',
        'Hamburg', 'Antwerp', 'New York', 'New Jersey', 'Virginia', 'Savannah',
        # Additional Key Ports
        'Genoa', 'Felixstowe', 'Le Havre', 'Southampton', 'Charleston', 'Savannah'
    ],
    
    # Tier 3: SVP Decision Triggers (Specific Impacts)
    'impact_events': [
        # Port Operations (Direct Impact)
        'congestion', 'port congestion', 'port closure', 'port suspension', 'port disruption',
        'port delay', 'port backlog', 'port strike', 'port closure',
        # Shipping Operations (Schedule Impact)
        'delay', 'delays', 'disruption', 'disruptions', 'blank sailing', 'schedule changes',
        'service suspension', 'route changes', 'capacity constraints',
        # Cost Impacts (Financial Impact)
        'freight rate hike', 'rate hike', 'surcharge', 'fee increase', 'cost increase',
        'price hike', 'price surge', 'rate surge', 'tariff increase',
        # Safety & Security (Risk Impact)
        'ship attack', 'piracy', 'detention', 'seizure', 'collision', 'grounding',
        'accident', 'incident', 'mechanical failure', 'weather disruption',
        # Supply Chain Impacts (Operational Impact)
        'shortage', 'shortages', 'bottleneck', 'bottlenecks', 'capacity constraints',
        'labor shortage', 'equipment shortage', 'supply chain disruption',
        'inventory shortage', 'stockout', 'delivery delays', 'customs delays',
        # Market Impacts (Business Impact)
        'oil price', 'oil prices', 'crude oil', 'natural gas', 'energy prices',
        'polymer prices', 'plastic prices', 'feedstock prices', 'commodity prices',
        'inflation', 'deflation', 'recession', 'market volatility',
        # Business Performance (Strategic Impact)
        'profit warning', 'revenue decline', 'margin pressure', 'earnings report',
        'demand surge', 'demand drop', 'capacity issues', 'overcapacity',
        'underutilization', 'cost cutting', 'restructuring'
    ],
    
    # Tier 4: The "Noise" Filter (Remove Non-Logistics)
    'blacklist': [
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'lifestyle', 'culture', 'tourism', 
        'hospitality', 'real estate', 'entertainment', 'stock market', 'fintech', 'celebrity', 'sports',
        'politics', 'election', 'elections', 'cryptocurrency', 'bitcoin', 'nft', 'gaming', 'fashion',
        'food', 'restaurant', 'retail', 'consumer', 'personal finance', 'technology', 'social media',
        'venture capital', 'funding', 'investment banking', 'startup', 'AI', 'artificial intelligence'
    ]
}

# Email Configuration
EMAIL_CONFIG = {
    'recipient': 'sc.sentinelnews@gmail.com',
    'sender': 'sc.sentinelnews@gmail.com',
    'subject_prefix': '🚢 SVP Logistics Alert - Borouge/ADNOC Impact Analysis',
    'max_items': 5
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 6,
    'max_summary_length': 250
}
