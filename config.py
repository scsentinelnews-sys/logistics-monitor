# RSS Feed Configuration - Precision Targeting
RSS_SOURCES = {
    'maritime_executive': 'https://www.maritime-executive.com/pressreleases.rss',
    'gcaptain': 'https://gcaptain.com/feed/',
    'lloyds_list': 'https://www.lloydslist.com/rss/ports-and-logistics',
    'the_maritime_standard': 'https://www.themaritimestandard.com/category/uae/feed/',
    'joc_logistics': 'https://www.joc.com/rss.xml',
}

# Precision Targeting - SVP Actionable Intelligence
BOURUGE_RELEVANCE = {
    # Tier 1: Primary Stakeholders (Must mention at least one)
    'entities': [
        'Borouge', 'ADNOC', 'L&S', 'Nimex', 'MAERSK', 'MSC', 'CMA CGM', 
        'Hapag-Lloyd', 'ONE', 'Evergreen', 'COSCO'
    ],
    # Tier 2: Actionable Locations
    'ports_routes': [
        'Khalifa Port', 'Jebel Ali', 'Ruways', 'Ruwais', 'Suez Canal', 
        'Strait of Hormuz', 'Red Sea', 'Bab el-Mandeb', 'Sohar'
    ],
    # Tier 3: Operational Impact Triggers
    'impact_events': [
        'congestion', 'delay', 'blank sailing', 'force majeure', 'surcharge', 
        'strike', 'closure', 'suspension', 'explosion', 'attack', 'detention'
    ],
    # Tier 4: The "Noise" Filter (Blacklist)
    'blacklist': [
        'hero', 'award', 'biography', 'lifestyle', 'culture', 'tourism', 
        'hospitality', 'real estate', 'entertainment', 'stock market', 'fintech'
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
