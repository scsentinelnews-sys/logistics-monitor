import os

RSS_SOURCES = {
    'emirates_news_agency': 'https://www.wam.ae/en/rss/all',
    'logistics_middle_east': 'https://www.logisticsmiddleeast.com/rss',
    'maritime_executive': 'https://maritime-executive.com/shipping-news/rss',
    'gcaptain_maritime': 'https://gcaptain.com/feed/',
    'splash_247': 'https://splash247.com/feed/'
}

BOURUGE_RELEVANCE = {
    'entities': ['ADNOC', 'Borouge', 'Khalifa Port', 'Jebel Ali', 'AD Ports', 'DP World'],
    'ports_routes': ['Salalah', 'Sohar', 'Duqm', 'Jeddah', 'Dammam', 'Hormuz', 'Suez'],
    'impact_events': ['attack', 'drone', 'missile', 'blocked', 'closure', 'delay', 'congestion'],
    'blacklist': ['car loan', 'dealership', 'passenger vehicle', 'retail banking', 'bitcoin', 'crypto']
}

GCC_RELEVANCE = {
    'countries': ['oman', 'saudi', 'ksa', 'kuwait', 'qatar', 'bahrain', 'uae', 'emirates'],
    'ports': ['salalah', 'sohar', 'duqm', 'jeddah', 'dammam', 'neom', 'khalifa', 'jebel ali', 'fujairah', 'ras al khaimah', 'ruwais', 'khor fakkan'],
    'security_terms': ['drone', 'attack', 'explosion', 'seized', 'blocked', 'uav', 'missile', 'gps spoofing']
}

EMAIL_CONFIG = {
    'subject_prefix: 🚢 Global Logistics Alert',
    'max_items': 5
}

MONITORING_CONFIG = {
    'check_interval_minutes': 30,
    'alert_window_hours': 0.5
}
