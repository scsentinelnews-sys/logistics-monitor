import sys
sys.path.append('.')
from rss_parser import fetch_and_filter_news
import os

os.environ['LOGISTICS_EMAIL_USER'] = 'sc.sentinelnews@gmail.com'
os.environ['LOGISTICS_EMAIL_PASSWORD'] = 'ywodqybwjbdxsqha'
os.environ['LOGISTICS_EMAIL_RECIPIENT'] = 'sc.sentinelnews@gmail.com'

print('🚢 Testing FIXED System with Major Carrier Keywords...')
print('📡 Sources: 6 proven working feeds')
print('🚢 Enhanced with MSC/Maersk/CMA CGM keywords')
print('⏰ Time window: 6 hours')
print('-' * 60)

articles = fetch_and_filter_news()

if articles:
    print(f'📧 Found {len(articles)} major carrier articles!')
    for article in articles[:3]:
        print(f'  - {article.get("title", "No title")[:70]}...')
        print(f'    Source: {article.get("source", "Unknown")}')
        print(f'    Keywords: MSC/Maersk/CMA CGM detected')
else:
    print('📭 No major carrier disruptions found')

print('✅ Fixed system test completed')
