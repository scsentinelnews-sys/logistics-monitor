import os

# NewsAPI Configuration
NEWS_API_CONFIG = {
    'base_url': 'https://newsapi.org/v2/everything',
    'api_key': os.getenv('NEWS_API_KEY'),
    'language': 'en',
    'sort_by': 'publishedAt',
    'page_size': 20,
    'time_window_hours': 6  # Look back 6 hours for fresh news
}

# Port Incident Target Configuration
PORT_INCIDENT_TARGETS = {
    'materials': [
        'Polyethylene', 'Polypropylene', 'Polymers', 
        'Crude Oil', 'LNG', 'Chemicals', 
        'Hazardous Materials', 'Petrochemicals'
    ],
    'infrastructure': [
        'Port Ruwais', 'Khalifa Port', 'Jebel Ali',
        'National Oil Company', 'L&S fleet', 'Abu Dhabi'
    ],
    'exclusions': [
        'cars', 'retail', 'food', 'consumer', 
        'passenger', 'automotive', 'dealership', 
        'supermarket', 'restaurant'
    ]
}

# Email Configuration
EMAIL_CONFIG = {
    'subject_prefix': '🚢 Port Incident Alert',
    'max_items': 10,
    'recipients': os.getenv('LOGISTICS_EMAIL_RECIPIENT')
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 6
}
