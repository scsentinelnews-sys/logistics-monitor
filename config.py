import os

# RSS Feed Configuration - Authoritative Sources Only
RSS_SOURCES = {
    # Top-Tier Authoritative Business News (High Credibility)
    'reuters_business': 'https://www.reuters.com/rssFeed/businessNews',
    'bbc_business': 'https://feeds.bbci.co.uk/news/business/rss.xml',
    'financial_times': 'https://www.ft.com/rss/companies',
    'guardian_business': 'https://www.theguardian.com/business/rss',
    'bloomberg_business': 'https://www.bloomberg.com/markets/news.rss',
    
    # Authoritative Financial Markets (Verified Sources)
    'wall_street_journal': 'https://feeds.wsj.com/xml/rss/3_7455.xml',
    'marketwatch': 'https://www.marketwatch.com/rss/topstories',
    'cnbc_business': 'https://www.cnbc.com/id/100003114/device/rss/rss.html',
    'yahoo_finance': 'https://finance.yahoo.com/news/rssindex',
    
    # Authoritative Logistics & Shipping (Industry-Standard Sources)
    'joc_container': 'https://www.joc.com/rss.xml',
    'splash247': 'https://splash247.com/feed/',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
    'lloyds_list': 'https://www.lloydslist.com/rss.xml',
    
    # Authoritative Energy & Commodities (Verified Sources)
    'platts_oil': 'https://www.platts.com/rss/platts-oil-news',
    'icis_energy': 'https://www.icis.com/rss/',
    'argus_media': 'https://www.argusmedia.com/rss.xml',
    
    # Authoritative UAE Sources (Local Credibility)
    'wam_uae': 'https://www.wam.ae/rss.xml',
    'the_national': 'https://www.thenationalnews.com/rss',
    'gulf_news': 'https://gulfnews.com/rss/business'
}

# Enhanced Logistics Intelligence - Authoritative Sources Focus
BOURUGE_RELEVANCE = {
    # Tier 1: Primary Stakeholders (Decision Impact)
    'entities': [
        # Major Container Lines (Highest Priority)
        'MAERSK', 'MSC', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO', 'HMM', 'Yang Ming', 'Zim', 'PIL',
        # Logistics & Shipping Terms (Direct Impact)
        'shipping', 'container', 'vessel', 'port', 'logistics', 'freight', 'cargo', 'tanker', 'carrier', 'shipping line',
        'supply chain', 'warehouse', 'distribution', 'transport', 'delivery', 'trucking', 'railway',
        # ADNOC & Borouge (UAE Priority)
        'ADNOC', 'Borouge', 'Abu Dhabi National Oil Company',
        # Additional Business Entities (Market Impact)
        'DHL', 'FedEx', 'UPS', 'DB Schenker', 'Kuehne + Nagel', 'Expeditors',
        'Walmart', 'Amazon', 'Target', 'Home Depot', 'IKEA', 'Tesla',
        # Energy & Commodities (Logistics Impact Only)
        'Shell', 'BP', 'ExxonMobil', 'Chevron', 'TotalEnergies',
        'OPEC', 'IEA',
        # UAE Specific Entities
        'Abu Dhabi Ports', 'DP World', 'Etihad Rail', 'Emirates Shipping'
    ],
    
    # Tier 2: Critical Locations (Operations Impact)
    'ports_routes': [
        # UAE Critical Locations (Highest Priority)
        'Ruwais', 'Ruwais Abu Dhabi', 'Ruwais UAE', 'Ruwais industrial', 'Ruwais refinery', 'Ruwais complex',
        'Khalifa Port', 'Khalifa Industrial Zone', 'Khalifa Port Abu Dhabi',
        'Jebel Ali', 'Jebel Ali Port', 'Jebel Ali Free Zone', 'Jebel Ali Terminal',
        'Fujairah', 'Fujairah Port', 'Fujairah Terminal', 'Fujairah Shipyard',
        'Abu Dhabi', 'Dubai', 'Sharjah', 'Sohar', 'Mussafah',
        'Mina Jebel Ali', 'Mina Zayed', 'Mina Khalifa',
        # ADNOC/Borouge Specific Locations
        'Borouge plant', 'Borouge complex', 'Borouge facility', 'Borouge polymer plant',
        'ADNOC processing', 'ADNOC refinery', 'ADNOC headquarters', 'ADNOC office',
        'ADNOC terminal', 'ADNOC depot', 'ADNOC distribution',
        # Global Maritime Chokepoints (Supply Chain Impact)
        'Strait of Hormuz', 'Bab el-Mandeb', 'Suez Canal', 'Strait of Malacca', 'Panama Canal',
        'Persian Gulf', 'Gulf of Oman', 'Arabian Gulf',
        # Major Global Ports (Operations Impact)
        'Singapore', 'Rotterdam', 'Shanghai', 'Ningbo', 'Hong Kong', 'Busan', 'Los Angeles', 'Long Beach',
        'Hamburg', 'Antwerp', 'New York', 'New Jersey', 'Virginia', 'Savannah', 'Genoa', 'Felixstowe', 'Le Havre', 'Southampton', 'Charleston',
        # Additional Key Locations
        'Middle East', 'Gulf region', 'Red Sea', 'Cape of Good Hope', 'Indian Ocean', 'Mediterranean Sea'
    ],
    
    # Tier 3: Decision Triggers (Logistics-Focused Impacts)
    'impact_events': [
        # Service Operations (Highest Priority)
        'resume', 'resumes', 'resumed', 'restart', 'service resume', 'vessels resume',
        'suspension', 'suspended', 'service suspension', 'blank sailing', 'cancellation',
        'delay', 'delays', 'disruption', 'disruptions', 'schedule changes', 'route changes',
        # Security & Safety Incidents (Critical Priority)
        'fire', 'fire attack', 'attack', 'hit', 'strike', 'assault', 'explosion', 'blast',
        'security breach', 'sabotage', 'incident', 'accident', 'security incident', 'terror attack',
        'emergency', 'crisis', 'damage', 'destruction', 'threat', 'warning', 'alert',
        # Port Operations (Direct Impact)
        'congestion', 'port congestion', 'port closure', 'port suspension', 'port disruption',
        'port delay', 'port backlog', 'port strike', 'severe disruption', 'yard congestion',
        'bottleneck', 'bottlenecks', 'overcapacity', 'underutilization',
        # Shipping Operations (Schedule Impact)
        'vessel', 'ship', 'container ship', 'tanker', 'carrier', 'shipping line',
        'reroute', 'reroutes', 'detour', 'detours', 'capacity constraints',
        # Market & Cost Impacts (Logistics-Focused Only)
        'freight rates', 'rate surge', 'price surge', 'cost increase', 'surcharge', 'rate hike',
        'shortage', 'shortages', 'equipment shortage', 'container shortage', 'labor shortage',
        # Production & Operations Impact (Direct Impact)
        'production halt', 'shutdown', 'operational disruption', 'facility damage',
        'plant closure', 'refinery shutdown', 'processing disruption', 'manufacturing halt',
        # Safety & Security (Risk Impact)
        'ship attack', 'piracy', 'detention', 'seizure', 'collision', 'grounding',
        'mechanical failure', 'weather disruption', 'security concerns',
        # Supply Chain Impacts (Operational Impact)
        'customs delay', 'technical issue', 'operational issue', 'pile up', 'piling up',
        'bound containers', 'gulf-bound', 'transit time', 'lead time'
    ],
    
    # Tier 4: Enhanced Blacklist (Filter Non-Logistics Content)
    'blacklist': [
        # Technology & AI (Filter Out)
        'nvidia', 'artificial intelligence', 'machine learning', 'thinking machines',
        'mira murati', 'openai', 'chatgpt', 'technology', 'tech', 'software', 'startup',
        'venture capital', 'funding', 'investment', 'significant investment', 'lab',
        'research lab', 'innovation', 'digital', 'automation', 'robotics',
        
        # General Oil/Market News (Filter Out)
        'oil price', 'oil prices', 'crude oil price', 'crude oil prices', 'energy prices',
        'stock market', 'share price', 'stock price', 'market analysis', 'trading',
        'earnings report', 'quarterly earnings', 'profit warning', 'revenue',
        'economic data', 'inflation data', 'gdp growth', 'interest rates',
        
        # Non-Logistics Business (Filter Out)
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'lifestyle', 'culture', 'tourism', 
        'hospitality', 'real estate', 'entertainment', 'fintech', 'celebrity', 'sports',
        'politics', 'election', 'elections', 'cryptocurrency', 'bitcoin', 'nft', 'gaming', 'fashion',
        'social media', 'investment banking', 'personal finance',
        
        # General Business (Filter Out)
        'retail sales', 'consumer spending', 'auto sales', 'housing market', 'job market',
        'corporate earnings', 'business news', 'company news', 'executive news'
    ]
}

# Email Configuration - No hardcoded credentials
EMAIL_CONFIG = {
    'recipient': os.getenv('LOGISTICS_EMAIL_RECIPIENT'),
    'sender': os.getenv('LOGISTICS_EMAIL_USER'),
    'subject_prefix': '🚢 Logistics Alert - Authoritative Sources Only',
    'max_items': 5
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 6,
    'max_summary_length': 250
}
