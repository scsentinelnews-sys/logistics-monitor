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
    
    # Supply Chain & Energy Markets
    'icis_chemical_logistics': 'https://www.icis.com/explore/resources/news/',
    'freightwaves_global': 'https://www.freightwaves.com/feed',
    'loadstar_supply_chain': 'https://theloadstar.com/feed/',
    'argus_media_energy': 'https://www.argusmedia.com/en/rss-feeds'
}

# Enhanced Precision Filtering Logic - Professional Logistics Intelligence
BOURUGE_RELEVANCE = {
    # GATE 1: PRIMARY STAKEHOLDERS (ADNOC/Borouge + Industry Standards)
    'entities': [
        # ADNOC/Borouge Specific (Your Core Business - Internal Use Only)
        'ADNOC', 'Borouge', 'Abu Dhabi National Oil Company', 'ADNOC Group', 'ADNOC Distribution',
        'ADNOC Gas', 'ADNOC Refining', 'ADNOC Logistics', 'ADNOC Drilling', 'ADNOC Processing',
        'ADNOC Shipping', 'ADNOC Supply Chain', 'ADNOC Global', 'ADNOC International',
        'Borouge Global', 'Borouge International', 'Borouge Supply Chain', 'Borouge Logistics',
        'Borouge Distribution', 'Borouge Manufacturing', 'Borouge Petrochemical',
        'Borouge Plastics', 'Borouge Polymers', 'L&S', 'Nimex',
        
        # Industry Standards (Professional Terms)
        'Petrochemical', 'Polymer', 'Polyethylene', 'Polypropylene', 
        'National Oil Company', 'Energy Major', 'Major Producer',
        'State-owned enterprise', 'Plastics Industry', 'Chemical Logistics',
        
        # Major Container Lines (Global Logistics Partners)
        'MAERSK', 'MSC', 'CMA CGM', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO', 'HMM', 'Yang Ming', 'Zim', 'PIL',
        
        # Logistics & Shipping Terms
        'shipping', 'container', 'vessel', 'port', 'logistics', 'freight', 'cargo', 'tanker', 'carrier', 'shipping line'
    ],
    
    # GATE 2: LOGISTICS CONTEXT (Professional + Strategic Locations)
    'ports_routes': [
        # UAE/Gulf Critical Locations (Strategic)
        'Khalifa Port', 'Jebel Ali', 'Abu Dhabi', 'Dubai', 'Ruways', 'Ruwais', 'Fujairah', 'Sohar',
        
        # Global Maritime Chokepoints (Strategic)
        'Suez Canal', 'Strait of Hormuz', 'Bab el-Mandeb', 'Strait of Malacca', 'Panama Canal',
        
        # Major Global Ports (Global Supply Chain)
        'Singapore', 'Rotterdam', 'Shanghai', 'Ningbo', 'Hong Kong', 'Busan', 'Los Angeles', 'Long Beach',
        'Hamburg', 'Antwerp', 'New York', 'New Jersey', 'Virginia', 'Savannah',
        
        # Professional Context Keywords
        'freight rates', 'container shipping', 'vessel diversion', 'blank sailing',
        'port congestion', 'Red Sea', 'supply chain disruption',
        'charter rates', 'bunker adjustment'
    ],
    
    # GATE 3: OPERATIONAL IMPACT TRIGGERS (Professional Events)
    'impact_events': [
        # Disruptions & Delays (Professional Terms)
        'congestion', 'delay', 'delays', 'disruption', 'disruptions', 'blank sailing', 'force majeure',
        
        # Operational Issues (Professional Terms)
        'strike', 'closure', 'closures', 'suspension', 'suspensions', 'shutdown', 'shutdowns',
        
        # Safety & Security (Professional Terms)
        'attack', 'attacks', 'detention', 'detentions', 'piracy', 'incident', 'accident',
        
        # Market & Cost Impacts (Professional Terms)
        'surcharge', 'rate hike', 'rate increase', 'shortage', 'shortages', 'bottleneck', 'bottlenecks',
        
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
        'worldwide incident', 'port congestion', 'port closure', 'port suspension', 'port disruption',
        'port delay', 'port backlog', 'port strike', 'severe disruption', 'yard congestion',
        'overcapacity', 'underutilization', 'reroute', 'reroutes', 'detour', 'detours',
        'capacity constraints', 'global shipping', 'international shipping', 'worldwide vessel',
        'polymer prices', 'plastic prices', 'petrochemical prices', 'feedstock prices',
        'global market', 'international market', 'worldwide pricing', 'ship attack', 'seizure',
        'collision', 'grounding', 'mechanical failure', 'weather disruption', 'security concerns',
        'customs delay', 'technical issue', 'operational issue', 'pile up', 'piling up',
        'bound containers', 'gulf-bound', 'transit time', 'lead time', 'global supply chain',
        'international supply chain', 'worldwide logistics'
    ],
    
    # GATE 4: ENHANCED BLACKLIST (Filter Non-Logistics Content)
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
        
        # Comprehensive Blacklist
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
        'venture capital', 'funding', 'investment', 'significant investment', 'lab',
        'research lab', 'innovation', 'digital', 'automation', 'robotics',
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

# Monitoring Configuration - Professional Settings
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 24,
    'max_summary_length': 250,
    'alert_threshold_hours': 24,
    'summary_min_length': 50,
    'summary_max_length': 250,
    'max_daily_items': 5
}
