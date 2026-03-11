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

# Enhanced 2026 Precision Filtering Logic - Comprehensive GCC Coverage
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
        
        # GCC Ports & Terminals (NEW: Comprehensive Coverage)
        'Salalah Port', 'Port of Salalah', 'Oman Port', 'Mina Sultan Qaboos', 'Sohar Port',
        'Port of Sohar', 'Duqm Port', 'Oman Logistics', 'Oman Shipping',
        'Jeddah Port', 'King Abdullah Port', 'Dammam Port', 'Ras Al Khair Port',
        'Yanbu Port', 'Port of Jeddah', 'Saudi Ports Authority', 'Mawani',
        'Kuwait Port', 'Shuwaikh Port', 'Shuaiba Port', 'Kuwait Shipping',
        'Bahrain Port', 'Khalifa Bin Salman Port', 'Bahrain Logistics',
        'Qatar Port', 'Hamad Port', 'Doha Port', 'Qatar Shipping',
        
        # GCC Shipping Lines & Logistics (NEW: Regional Coverage)
        'Oman Shipping', 'National Shipping Company of Oman', 'Kuwait Oil Tanker',
        'Bahrain Shipping', 'Qatar Shipping', 'Saudi Shipping', 'GCC Shipping',
        
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
    
    # GATE 2: LOGISTICS CONTEXT (GCC + Strategic Locations)
    'ports_routes': [
        # UAE Critical Ports & Terminals (Primary Focus)
        'Khalifa Port', 'Jebel Ali Port', 'Ruwais', 'Ruwais Port', 'Ruwais Terminal', 'Ruwais Distribution Center',
        'AD Ports', 'KIZAD', 'Khalifa Industrial Zone Abu Dhabi', 'KIZAD Abu Dhabi',
        'Abu Dhabi Ports', 'DP World UAE', 'Abu Dhabi Terminals', 'Mina Jebel Ali', 'Mina Zayed', 'Mina Khalifa',
        'Jebel Ali Free Zone', 'Jebel Ali Terminal', 'Port of Jebel Ali', 'Port of Khalifa',
        
        # GCC Critical Ports & Terminals (NEW: Comprehensive Coverage)
        'Salalah', 'Port of Salalah', 'Oman', 'Mina Sultan Qaboos', 'Sohar', 'Port of Sohar', 'Duqm', 'Duqm Port',
        'Jeddah', 'Port of Jeddah', 'King Abdullah Port', 'Dammam', 'Port of Dammam', 'Ras Al Khair', 'Yanbu', 'Port of Yanbu',
        'Kuwait', 'Shuwaikh Port', 'Shuaiba Port', 'Bahrain', 'Khalifa Bin Salman Port', 'Qatar', 'Hamad Port', 'Doha Port',
        
        # UAE Additional Ports
        'Abu Dhabi', 'Dubai', 'Sharjah', 'Sohar', 'Fujairah', 'Ras Al Khaimah', 'Umm Al Quwain', 'Ajman',
        'Fujairah Port', 'Sharjah Port', 'Ajman Port', 'Umm Al Quwain Port', 'Ras Al Khaimah Port',
        
        # UAE Industrial Areas
        'Mussafah', 'Industrial City', 'Mussafah Industrial Area', 'ICAD', 'Abu Dhabi Industrial City',
        
        # GCC Industrial Areas (NEW: Regional Coverage)
        'Ras Al Khaimah', 'Ras Al Khaimah Port', 'Oman Industrial Area', 'Salalah Industrial Zone',
        'Jeddah Industrial Area', 'Dammam Industrial Area', 'Kuwait Industrial Area',
        
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
    
    # GATE 3: 2026 OPERATIONAL IMPACT TRIGGERS (Enhanced with GCC Focus)
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
        
        # Port & Terminal Operations (GCC Focus)
        'port congestion', 'terminal congestion', 'port closure', 'terminal closure',
        'port delay', 'terminal delay', 'port disruption', 'terminal disruption',
        'port operations', 'terminal operations', 'yard congestion', 'terminal yard',
        'berth delay', 'berth congestion', 'container yard', 'container terminal',
        
        # Development & Expansion (GCC Focus)
        'expansion', 'development', 'capacity increase', 'new terminal', 'terminal development',
        'infrastructure', 'digital transformation', 'modernization', 'upgrade', 'improvement',
        
        # GCC Maritime Security (NEW: Regional Security Focus)
        'drone attack', 'missile attack', 'security incident', 'maritime security',
        'blocked', 'vessel blocked', 'strait blocked', 'hormuz blocked', 'red sea blocked',
        'gulf security', 'gcc security', 'middle east security', 'regional security',
        
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
    
    # GATE 4: ENHANCED BLACKLIST (Fixed - Removed False Positives)
    'blacklist': [
        # Automotive Industry (Filter Out - Not Logistics)
        'car loan', 'subprime', 'consumer credit', 'retail banking',
        'automotive', 'automobile', 'luxury car', 'luxury cars', 'auto sales', 'vehicle sales',
        'vw', 'volkswagen', 'toyota', 'honda', 'ford', 'general motors', 'gm', 'bmw', 'mercedes', 'tesla',
        'car insurance', 'auto insurance', 'vehicle insurance', 'dealership', 'dealerships',
        
        # Energy Industry (Filter Out - Unless Logistics Impact)
        'shell', 'bp', 'exxon', 'chevron', 'total', 'equinor',
        'clean energy', 'renewable energy', 'solar', 'wind', 'battery', 'batteries',
        'oil price', 'oil prices', 'energy price', 'energy prices', 'gas price', 'gas prices',
        'energy crisis', 'energy market', 'energy trading', 'energy investment',
        'brazil', 'brazilian', 'argentina', 'mexico', 'chile', 'colombia', 'peru',
        
        # Financial Services (Filter Out - Not Logistics)
        'subprime firm', 'goeasy', 'higher losses',
        'loan', 'loans', 'lending', 'credit', 'credit risk', 'financial services',
        'banking', 'banks', 'investment', 'investments', 'stock market', 'equity', 'shares',
        
        # Professional "Noise" Filter
        'real estate', 'hospitality', 'tourism', 'sports', 'celebrity', 
        'lifestyle', 'fintech', 'bitcoin', 'crypto', 'fashion', 'retail sales',
        
        # Comprehensive Blacklist (Removed logistics terms and false positives)
        'hero', 'heroes', 'economic hero', 'award', 'awards', 'biography', 'culture', 
        'entertainment', 'driving', 'economy', 'economic',
        'politics', 'election', 'elections', 'cryptocurrency', 'bitcoin', 'nft', 'gaming',
        'social media', 'investment banking', 'personal finance',
        'corporate earnings', 'business news', 'company news', 'executive news',
        'hmt', 'reform hmt', 'british shipping', 'uk shipping policy',
        'spirit airlines', 'southwest', 'delta', 'united', 'american airlines',
        'jetblue', 'alaska airlines', 'frontier', 'allegiant', 'amazon', 'apple', 'google',
        'microsoft', 'meta', 'witkoff', 'trump', 'russia', 'iran', 'ukraine',
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

# config.py updates
# REMOVE 'car' from blacklist -> REPLACE with 'car loan', 'dealership', 'passenger vehicle'
# REMOVE 'saudi', 'oman', 'kuwait' from any blacklists.

# Updated GCC_RELEVANCE for 100% Coverage
GCC_RELEVANCE = {
    'countries': [
        'oman', 'saudi', 'ksa', 'kuwait', 'qatar', 'bahrain', 'uae', 'emirates'
    ],
    'ports': [
        # UAE
        'khalifa', 'jebel ali', 'fujairah', 'ras al khaimah', 'ruwais', 
        'khor fakkan', 'mina zayed', 'hamriya', 'mina khalid', 'ajman',
        # SAUDI ARABIA
        'jeddah', 'dammam', 'neom', 'yanbu', 'jubail', 'king abdullah port', 
        'ras al khair', 'ras tanura', 'jazan', 'dhiba',
        # OMAN
        'salalah', 'sohar', 'duqm', 'muscat', 'khasab', 'mina al fahal',
        # QATAR
        'hamad', 'ras laffan', 'mesaieed', 'doha port',
        # KUWAIT
        'shuaiba', 'shuwaikh', 'doha',
        # BAHRAIN
        'khalifa bin salman', 'mina salman'
    ],
    'security_terms': [
        'drone', 'attack', 'explosion', 'seized', 'blocked', 'intercepted', 
        'uav', 'missile', 'gps spoofing', 'gnss', 'vessel held', 'strait of hormuz'
    ]
}
