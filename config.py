import os

# RSS Feed Configuration - High-Reliability Logistics Sources
RSS_SOURCES = {
    # Regional Strategic News (UAE/GCC Focus)
    'emirates_news_agency': 'https://www.wam.ae/en/rss/all',
    'logistics_middle_east': 'https://www.logisticsmiddleeast.com/rss',
    'gulf_business_trade': 'https://gulfbusiness.com/feed/',
    
    # Global Maritime & Container Intelligence
    'maritime_executive': 'https://maritime-executive.com/shipping-news/rss',
    'gcaptain_maritime': 'https://gcaptain.com/feed/',
    'splash_247': 'https://splash247.com/feed/',
    'hellenic_shipping': 'https://www.hellenicshippingnews.com/feed/',
'augusmedia':
'https://www.argusmedia.com/en/news-and-insights/latest-market-news/'
    
    # Supply Chain & Energy Markets
    'icis_chemical_logistics': 'https://www.icis.com/explore/resources/news/',
    'freightwaves_global': 'https://www.freightwaves.com/feed',
    'loadstar_supply_chain': 'https://theloadstar.com/feed/',
    'argus_media_energy': 'https://www.argusmedia.com/en/rss-feeds'
}

# Enhanced 2026 Precision Filtering Logic - UAE Ports & Logistics Focus
BOURUGE_RELEVANCE = {
    # GATE 1: PRIMARY STAKEHOLDERS (ADNOC/Borouge + UAE Logistics Providers)
    'entities': [
        # ADNOC/Borouge Specific (Your Core Business - Internal Use Only)
        'ADNOC', 'Borouge', 'Abu Dhabi National Oil Company', 'ADNOC Group', 'ADNOC Distribution',
        'ADNOC Gas', 'ADNOC Refining', 'ADNOC Logistics', 'ADNOC Drilling', 'ADNOC Processing',
        'ADNOC Shipping', 'ADNOC Supply Chain', 'ADNOC Global', 'ADNOC International',
        'Borouge Global', 'Borouge International', 'Borouge Supply Chain', 'Borouge Logistics',
        'Borouge Distribution', 'Borouge Manufacturing', 'Borouge Petrochemical',
        'Borouge Plastics', 'Borouge Polymers', 'L&S', 'Nimex',
        
        # UAE Ports & Terminals (Primary Logistics Service Providers)
        'Khalifa Port', 'Jebel Ali Port', 'Ruwais Distribution Center', 'AD Ports', 'KIZAD',
        'Abu Dhabi Ports', 'DP World', 'Abu Dhabi Terminals', 'Khalifa Industrial Zone',
        'Khalifa Port Abu Dhabi', 'Jebel Ali Free Zone', 'Jebel Ali Terminal', 'Mina Jebel Ali',
        'Mina Zayed', 'Mina Khalifa', 'Port of Jebel Ali', 'Port of Khalifa',
        'Jebel Ali Port Authority', 'Abu Dhabi Port Company',
        
        # Major UAE Logistics Hubs
        'Dubai Logistics City', 'Dubai Trade Center', 'Dubai Airport Free Zone',
        'Sharjah Airport International Free Zone', 'Ajman Free Zone', 'Umm Al Quwain Free Zone',
        'Ras Al Khaimah Free Zone', 'Fujairah Free Zone', 'Dubai Maritime City',
        
        # Global Container Lines (Partners)
        'MAERSK', 'MSC', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO', 'HMM', 'Yang Ming', 'Zim', 'PIL',
        
        # Global Logistics Providers
        'DHL', 'FedEx', 'UPS', 'DB Schenker', 'Kuehne + Nagel', 'Expeditors',
        
        # Industry Standards
        'Petrochemical', 'Polymer', 'Polyethylene', 'Polypropylene', 
        'National Oil Company', 'Energy Major', 'Major Producer',
        'State-owned enterprise', 'Plastics Industry', 'Chemical Logistics',
        
        # Logistics & Shipping Terms
        'shipping', 'container', 'vessel', 'port', 'logistics', 'freight', 'cargo', 'tanker', 'carrier', 'shipping line',
        'terminal', 'port terminal', 'container terminal', 'distribution center', 'logistics hub'
    ],
    
    # GATE 2: LOGISTICS CONTEXT (UAE + Strategic Locations)
    'ports_routes': [
        # UAE Critical Ports & Terminals (Primary Focus)
        'Khalifa Port', 'Jebel Ali Port', 'Ruwais', 'Ruwais Port', 'Ruwais Terminal', 'Ruwais Distribution Center',
        'AD Ports', 'KIZAD', 'Khalifa Industrial Zone Abu Dhabi', 'KIZAD Abu Dhabi',
        'Abu Dhabi Ports', 'DP World UAE', 'Abu Dhabi Terminals', 'Mina Jebel Ali', 'Mina Zayed', 'Mina Khalifa',
        'Jebel Ali Free Zone', 'Jebel Ali Terminal', 'Port of Jebel Ali', 'Port of Khalifa',
        
        # UAE Additional Ports
        'Abu Dhabi', 'Dubai', 'Sharjah', 'Sohar', 'Fujairah', 'Ras Al Khaimah', 'Umm Al Quwain', 'Ajman',
        'Fujairah Port', 'Sharjah Port', 'Ajman Port', 'Umm Al Quwain Port', 'Ras Al Khaimah Port',
        
        # UAE Industrial Areas
        'Mussafah', 'Industrial City', 'Mussafah Industrial Area', 'ICAD', 'Abu Dhabi Industrial City',
        
        # Global Maritime Chokepoints (Strategic)
        'Suez Canal', 'Strait of Hormuz', 'Bab el-Mandeb', 'Strait of Malacca', 'Panama Canal',
        
        # Major Global Ports (International Supply Chain)
        'Singapore', 'Rotterdam', 'Shanghai', 'Ningbo', 'Hong Kong', 'Busan', 'Los Angeles', 'Long Beach',
        'Hamburg', 'Antwerp', 'New York', 'New Jersey', 'Virginia', 'Savannah', 'Genoa', 'Felixstowe',
        
        # Professional Context Keywords
        'freight rates', 'container shipping', 'vessel diversion', 'blank sailing',
        'port congestion', 'Red Sea', 'supply chain disruption',
        'charter rates', 'bunker adjustment', 'terminal operations', 'port operations'
    ],
    
    # GATE 3: 2026 OPERATIONAL IMPACT TRIGGERS (Enhanced with UAE Port Focus)
    'impact_events': [
        # Disruptions & Delays (Professional Terms)
        'congestion', 'delay', 'delays', 'disruption', 'disruptions', 'blank sailing', 'force majeure',
        
        # Operational Issues (Professional Terms)
        'strike', 'closure', 'closures', 'suspension', 'suspensions', 'shutdown', 'shutdowns',
        
        # Safety & Security (Professional Terms)
        'attack', 'attacks', 'detention', 'detentions', 'piracy', 'incident', 'accident',
        
        # Market & Cost Impacts (Professional Terms)
        'surcharge', 'rate hike', 'rate increase', 'shortage', 'shortages', 'bottleneck', 'bottlenecks',
        
        # 2026 NEW TECHNICAL RISKS
        'GNSS', 'GPS spoofing', 'UAV', 'projectile', 'war risk surcharge', 'WRS',
        'blank sailing', 'diversion', 'Strait of Hormuz closure',
        
        # Port & Terminal Operations (UAE Focus)
        'port congestion', 'terminal congestion', 'port closure', 'terminal closure',
        'port delay', 'terminal delay', 'port disruption', 'terminal disruption',
        'port operations', 'terminal operations', 'yard congestion', 'terminal yard',
        'berth delay', 'berth congestion', 'container yard', 'container terminal',
        
        # Development & Expansion (UAE Port Focus)
        'expansion', 'development', 'capacity increase', 'new terminal', 'terminal development',
        'infrastructure', 'digital transformation', 'modernization', 'upgrade', 'improvement',
        
        # Comprehensive Impact Events
        'production halt', 'operational disruption', 'facility damage',
        'plant closure', 'refinery shutdown', 'processing disruption', 'manufacturing halt',
        'supply chain disruption', 'logistics disruption', 'distribution disruption',
        'global supply chain', 'international logistics', 'worldwide shipping',
        'resume', 'resumes', 'resumed', 'restart', 'service resume', 'vessels resume',
        'suspension', 'suspended', 'service suspension', 'cancellation',
        'schedule changes', 'route changes', 'global disruption', 'international disruption',
        'worldwide impact', 'fire', 'fire attack', 'assault', 'explosion', 'blast',
        'security breach', 'sabotage', 'security incident', 'terror attack', 'emergency', 'crisis',
        'damage', 'destruction', 'threat', 'warning', 'alert', 'global security', 'international security',
        'worldwide incident', 'port backlog', 'port strike', 'severe disruption', 'yard congestion',
        'overcapacity', 'underutilization', 'reroute', 'reroutes', 'detour', 'detours',
        'capacity constraints', 'global shipping', 'international shipping', 'worldwide vessel',
        'polymer prices', 'plastic prices', 'petrochemical prices', 'feedstock prices',
        'global market', 'international market', 'worldwide pricing', 'ship attack', 'seizure',
        'collision', 'grounding', 'mechanical failure', 'weather disruption', 'security concerns',
        'customs delay', 'technical issue', 'operational issue', 'pile up', 'piling up',
        'bound containers', 'gulf-bound', 'transit time', 'lead time', 'global supply chain',
        'international supply chain', 'worldwide logistics'
    ],
    
    # GATE 4: ENHANCED BLACKLIST (Fixed - Removed Logistics Terms)
    'blacklist': [
        # Automotive Industry (Filter Out - Not Logistics)
        'car', 'cars', 'automotive', 'automobile', 'vehicle', 'vehicles', 'suv', 'sedan', 'truck', 'trucks',
        'luxury car', 'luxury cars', 'car sales', 'auto sales', 'vehicle sales', 'automotive sales',
        'vw', 'volkswagen', 'toyota', 'honda', 'ford', 'general motors', 'gm', 'bmw', 'mercedes', 'tesla',
        'car loan', 'car loans', 'auto loan', 'auto loans', 'subprime', 'subprime firm', 'goeasy',
        'car insurance', 'auto insurance', 'vehicle insurance', 'dealership', 'dealerships',
        
        # Energy Industry (Filter Out - Unless Logistics Impact)
        'shell', 'bp', 'exxon', 'chevron', 'total', 'equinor', 'saudi aramco', 'aramco',
        'clean energy', 'renewable energy', 'solar', 'wind', 'battery', 'batteries',
        'oil price', 'oil prices', 'energy price', 'energy prices', 'gas price', 'gas prices',
        'energy crisis', 'energy market', 'energy trading', 'energy investment',
        
        # Professional "Noise" Filter
        'luxury car', 'passenger vehicle', 'automotive sales', 'VW', 'Toyota', 
        'real estate', 'hospitality', 'tourism', 'sports', 'celebrity', 
        'lifestyle', 'fintech', 'bitcoin', 'crypto', 'fashion', 'retail sales',
        
        # Comprehensive Blacklist (Removed logistics terms)
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'culture', 
        'entertainment', 'stock market', 'driving', 'economy', 'economic',
        'politics', 'election', 'elections', 'cryptocurrency', 'bitcoin', 'nft', 'gaming',
        'social media', 'investment banking', 'personal finance',
        'retail sales', 'consumer spending', 'auto sales', 'housing market', 'job market',
        'corporate earnings', 'business news', 'company news', 'executive news',
        'saudi', 'saudi arabian', 'hmt', 'reform hmt', 'british shipping', 'uk shipping policy',
        'spirit airlines', 'southwest', 'delta', 'united', 'american airlines',
        'jetblue', 'alaska airlines', 'frontier', 'allegiant', 'amazon', 'apple', 'google',
        'microsoft', 'meta', 'tesla', 'witkoff', 'trump', 'russia', 'iran', 'ukraine',
        'white house', 'pentagon', 'congress', 'senate', 'house of representatives',
        'prime minister', 'president', 'foreign minister', 'defense minister',
        'la terminals', 'bridge closure', 'local disruption', 'regional issue',
        'city council', 'state government', 'local politics', 'regional politics',
        'nvidia', 'artificial intelligence', 'machine learning', 'thinking machines',
        'mira murati', 'openai', 'chatgpt', 'technology', 'tech', 'software', 'startup',
        'venture capital', 'funding', 'significant investment', 'lab',
        'research lab', 'innovation', 'automation', 'robotics',
        'share price', 'stock price', 'market analysis', 'trading',
        'earnings report', 'quarterly earnings', 'profit warning', 'revenue',
        'economic data', 'inflation data', 'gdp growth', 'interest rates',
        
        # Additional Non-Logistics Terms
        'brazil', 'brazilian', 'argentina', 'mexico', 'chile', 'colombia', 'peru',
        'consumer', 'consumers', 'retail', 'retailing', 'shopping', 'mall', 'malls',
        'fashion', 'clothing', 'apparel', 'shoes', 'footwear', 'jewelry', 'watches',
        'restaurant', 'restaurants', 'food', 'beverage', 'travel', 'tourism', 'hotel', 'hotels'
    ]
}

# Email Configuration - Professional Subject Only
EMAIL_CONFIG = {
    'recipient': os.getenv('LOGISTICS_EMAIL_RECIPIENT'),
    'sender': os.getenv('LOGISTICS_EMAIL_USER'),
    'subject_prefix': '🚢 Global Logistics Alert',
    'max_items': 5
}

# Monitoring Configuration - 30-MINUTE TIME WINDOW
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 0.5,  # 30 MINUTES ONLY
    'max_summary_length': 250,
    'alert_threshold_hours': 0.5,  # 30 MINUTES ONLY
    'summary_min_length': 50,
    'summary_max_length': 250,
    'max_daily_items': 5
}
