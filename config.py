import os

# RSS Feed Configuration - Authoritative Sources Only
RSS_SOURCES = {
    # Top-Tier Authoritative Business News (High Credibility)
    'reuters_business': 'https://www.reuters.com/rss/world/rss',
    'bbc_business': 'https://feeds.bbci.co.uk/news/business/rss.xml',
    'financial_times': 'https://www.ft.com/rss/companies',
    'guardian_business': 'https://www.theguardian.com/business/rss',
    'cnbc_business': 'https://www.cnbc.com/id/100003114/device/rss/rss.html',
    'yahoo_finance': 'https://finance.yahoo.com/news/rssindex',
    'marketwatch': 'https://www.marketwatch.com/rss/topstories',
    
    # Authoritative Logistics & Shipping (Industry-Standard Sources)
    'joc_container': 'https://www.joc.com/rss.xml',
    'splash247': 'https://splash247.com/feed/',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
    'freightwaves': 'https://www.freightwaves.com/rss.xml',
    
    # Authoritative Energy & Commodities (Verified Sources)
    'icis_energy': 'https://www.icis.com/rss/',
    'platts_oil': 'https://www.platts.com/rss/platts-oil-news',
    'argus_media': 'https://www.argusmedia.com/rss.xml',
    
    # Authoritative UAE Sources (Local Credibility)
    'wam_uae': 'https://www.wam.ae/rss.xml',
    'the_national': 'https://www.thenationalnews.com/rss',
    'gulf_news': 'https://gulfnews.com/rss/business'
}

# Enhanced Logistics Intelligence - ADNOC/Borouge Global Logistics Impact Only
BOURUGE_RELEVANCE = {
    # Tier 1: Primary Entities (ADNOC/Borouge Global Logistics Business)
    'entities': [
        # Borouge & ADNOC (Highest Priority - Global Logistics Business)
        'ADNOC', 'Borouge', 'Abu Dhabi National Oil Company', 'ADNOC Group', 'ADNOC Distribution',
        'ADNOC Gas', 'ADNOC Refining', 'ADNOC Logistics', 'ADNOC Drilling', 'ADNOC Processing',
        'ADNOC Shipping', 'ADNOC Supply Chain', 'ADNOC Global', 'ADNOC International',
        'Borouge Global', 'Borouge International', 'Borouge Supply Chain', 'Borouge Logistics',
        'Borouge Distribution', 'Borouge Manufacturing', 'Borouge Petrochemical',
        
        # Major Container Lines (ADNOC/Borouge Global Logistics Partners)
        'MAERSK', 'MSC', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO', 'HMM', 'Yang Ming', 'Zim', 'PIL',
        
        # ADNOC/Borouge Key Global Logistics Partners
        'DHL', 'FedEx', 'UPS', 'DB Schenker', 'Kuehne + Nagel', 'Expeditors',
        
        # Major Retail Customers (ADNOC/Borouge Global Supply Chain)
        'Walmart', 'Amazon', 'Target', 'Home Depot', 'IKEA', 'Tesla',
        
        # Energy & Commodities (ADNOC/Borouge Global Market Impact)
        'Shell', 'BP', 'ExxonMobil', 'Chevron', 'TotalEnergies',
        'OPEC', 'IEA',
        
        # UAE Specific Entities (ADNOC/Borouge Global Infrastructure)
        'Abu Dhabi Ports', 'DP World', 'Etihad Rail', 'Emirates Shipping'
    ],
    
    # Tier 2: Critical Locations (ADNOC/Borouge Global Logistics Network)
    'ports_routes': [
        # UAE Critical ADNOC/Borouge Locations (Highest Priority)
        'Ruwais', 'Ruwais Abu Dhabi', 'Ruwais UAE', 'Ruwais industrial', 'Ruwais refinery', 'Ruwais complex',
        'Ruwais petrochemical', 'Ruwais manufacturing', 'Ruwais export terminal',
        'Khalifa Port', 'Khalifa Industrial Zone', 'Khalifa Port Abu Dhabi',
        'Jebel Ali', 'Jebel Ali Port', 'Jebel Ali Free Zone', 'Jebel Ali Terminal',
        'Fujairah', 'Fujairah Port', 'Fujairah Terminal', 'Fujairah Shipyard',
        'Abu Dhabi', 'Dubai', 'Sharjah', 'Sohar', 'Mussafah',
        'Mina Jebel Ali', 'Mina Zayed', 'Mina Khalifa',
        
        # ADNOC/Borouge Global Logistics Hubs
        'Borouge plant', 'Borouge complex', 'Borouge facility', 'Borouge polymer plant',
        'ADNOC processing', 'ADNOC refinery', 'ADNOC headquarters', 'ADNOC office',
        'ADNOC terminal', 'ADNOC depot', 'ADNOC distribution', 'ADNOC logistics hub',
        
        # ADNOC/Borouge International Logistics Routes (Global Impact)
        'Strait of Hormuz', 'Bab el-Mandeb', 'Suez Canal', 'Strait of Malacca', 'Panama Canal',
        'Persian Gulf', 'Gulf of Oman', 'Arabian Gulf',
        
        # Major Global Ports (ADNOC/Borouge Global Supply Chain)
        'Singapore', 'Rotterdam', 'Shanghai', 'Ningbo', 'Hong Kong', 'Busan', 'Los Angeles', 'Long Beach',
        'Hamburg', 'Antwerp', 'New York', 'New Jersey', 'Virginia', 'Savannah', 'Genoa', 'Felixstowe', 'Le Havre', 'Southampton', 'Charleston',
        
        # Additional Key Locations
        'Middle East', 'Gulf region', 'Red Sea', 'Cape of Good Hope', 'Indian Ocean', 'Mediterranean Sea'
    ],
    
    # Tier 3: Decision Triggers (ADNOC/Borouge Global Logistics Impact Only)
    'impact_events': [
        # ADNOC/Borouge Operations (Global Business Impact)
        'production halt', 'shutdown', 'operational disruption', 'facility damage',
        'plant closure', 'refinery shutdown', 'processing disruption', 'manufacturing halt',
        'supply chain disruption', 'logistics disruption', 'distribution disruption',
        'global supply chain', 'international logistics', 'worldwide shipping',
        
        # Service Operations (Global Business Impact)
        'resume', 'resumes', 'resumed', 'restart', 'service resume', 'vessels resume',
        'suspension', 'suspended', 'service suspension', 'blank sailing', 'cancellation',
        'delay', 'delays', 'disruption', 'disruptions', 'schedule changes', 'route changes',
        'global disruption', 'international disruption', 'worldwide impact',
        
        # Security & Safety Incidents (Global Infrastructure Impact)
        'fire', 'fire attack', 'attack', 'hit', 'strike', 'assault', 'explosion', 'blast',
        'security breach', 'sabotage', 'incident', 'accident', 'security incident', 'terror attack',
        'emergency', 'crisis', 'damage', 'destruction', 'threat', 'warning', 'alert',
        'global security', 'international security', 'worldwide incident',
        
        # Port Operations (Global Logistics Network Impact)
        'congestion', 'port congestion', 'port closure', 'port suspension', 'port disruption',
        'port delay', 'port backlog', 'port strike', 'severe disruption', 'yard congestion',
        'bottleneck', 'bottlenecks', 'overcapacity', 'underutilization',
        'global port', 'international port', 'worldwide port',
        
        # Shipping Operations (Global Supply Chain Impact)
        'vessel', 'ship', 'container ship', 'tanker', 'carrier', 'shipping line',
        'reroute', 'reroutes', 'detour', 'detours', 'capacity constraints',
        'global shipping', 'international shipping', 'worldwide vessel',
        
        # Market & Cost Impacts (Global Business Impact)
        'freight rates', 'rate surge', 'price surge', 'cost increase', 'surcharge', 'rate hike',
        'shortage', 'shortages', 'equipment shortage', 'container shortage', 'labor shortage',
        'polymer prices', 'plastic prices', 'petrochemical prices', 'feedstock prices',
        'global market', 'international market', 'worldwide pricing',
        
        # Safety & Security (Global Risk Management)
        'ship attack', 'piracy', 'detention', 'seizure', 'collision', 'grounding',
        'mechanical failure', 'weather disruption', 'security concerns',
        'global safety', 'international security',
        
        # Supply Chain Impacts (Global Business Operations)
        'customs delay', 'technical issue', 'operational issue', 'pile up', 'piling up',
        'bound containers', 'gulf-bound', 'transit time', 'lead time',
        'global supply chain', 'international supply chain', 'worldwide logistics'
    ],
    
    # Tier 4: Enhanced Blacklist (Filter Non-Global Logistics Impact Content)
    'blacklist': [
        # Technology & AI (Filter Out - No Global Logistics Impact)
        'nvidia', 'artificial intelligence', 'machine learning', 'thinking machines',
        'mira murati', 'openai', 'chatgpt', 'technology', 'tech', 'software', 'startup',
        'venture capital', 'funding', 'investment', 'significant investment', 'lab',
        'research lab', 'innovation', 'digital', 'automation', 'robotics',
        
        # General Oil/Market News (Filter Out - Unless Global Logistics Impact)
        'oil price', 'oil prices', 'crude oil price', 'crude oil prices', 'energy prices',
        'stock market', 'share price', 'stock price', 'market analysis', 'trading',
        'earnings report', 'quarterly earnings', 'profit warning', 'revenue',
        'economic data', 'inflation data', 'gdp growth', 'interest rates',
        
        # Non-ADNOC/Borouge Business (Filter Out - No Global Logistics Impact)
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'lifestyle', 'culture', 'tourism', 
        'hospitality', 'real estate', 'entertainment', 'fintech', 'celebrity', 'sports',
        'politics', 'election', 'elections', 'cryptocurrency', 'bitcoin', 'nft', 'gaming', 'fashion',
        'social media', 'investment banking', 'personal finance',
        
        # General Business (Filter Out - No Global Logistics Impact)
        'retail sales', 'consumer spending', 'auto sales', 'housing market', 'job market',
        'corporate earnings', 'business news', 'company news', 'executive news',
        
        # Non-ADNOC Energy Companies (Filter Out - No Global Logistics Impact)
        'saudi aramco', 'aramco', 'saudi', 'saudi arabian',
        'bp', 'shell', 'exxon', 'chevron', 'total', 'equinor',
        
        # Non-ADNOC/Borouge Shipping (Filter Out - No Global Logistics Impact)
        'hmt', 'reform hmt', 'british shipping', 'uk shipping policy',
        
        # Non-ADNOC/Borouge Airlines (Filter Out - No Global Logistics Impact)
        'spirit airlines', 'southwest', 'delta', 'united', 'american airlines',
        'jetblue', 'alaska airlines', 'frontier', 'allegiant',
        
        # Non-ADNOC/Borouge Technology (Filter Out - No Global Logistics Impact)
        'amazon', 'apple', 'google', 'microsoft', 'meta', 'tesla',
        'witkoff', 'trump', 'russia', 'iran', 'ukraine',
        
        # Non-ADNOC/Borouge Government/Politics (Filter Out - No Global Logistics Impact)
        'white house', 'pentagon', 'congress', 'senate', 'house of representatives',
        'prime minister', 'president', 'foreign minister', 'defense minister',
        
        # Local/Regional Issues (Filter Out - No Global Logistics Impact)
        'la terminals', 'bridge closure', 'local disruption', 'regional issue',
        'city council', 'state government', 'local politics', 'regional politics'
    ]
}

# Email Configuration - No hardcoded credentials
EMAIL_CONFIG = {
    'recipient': os.getenv('LOGISTICS_EMAIL_RECIPIENT'),
    'sender': os.getenv('LOGISTICS_EMAIL_USER'),
    'subject_prefix': '🚢 ADNOC/Borouge Global Logistics Impact Alert',
    'max_items': 5
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 6,
    'max_summary_length': 250
}
