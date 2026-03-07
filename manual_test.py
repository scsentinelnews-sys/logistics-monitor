import sys
sys.path.append('.')
from rss_parser import fetch_and_filter_news
import os

os.environ['LOGISTICS_EMAIL_USER'] = 'sc.sentinelnews@gmail.com'
os.environ['LOGISTICS_EMAIL_PASSWORD'] = 'ywodqybwjbdxsqha'
os.environ['LOGISTICS_EMAIL_RECIPIENT'] = 'sc.sentinelnews@gmail.com'

print('🚢 Manual Test in GitHub Actions...')
articles = fetch_and_filter_news()

if articles:
    print(f'📧 Found {len(articles)} major carrier articles!')
    for article in articles[:3]:
        print(f'  - {article.get("title", "No title")[:70]}...')
        print(f'    Source: {article.get("source", "Unknown")}')
else:
    print('📭 No major carrier disruptions found')

print('✅ Manual test completed')
