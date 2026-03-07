#!/usr/bin/env python3
import sys
sys.path.append('.')
from daily_summary import summary_tracker

print('📊 Sending daily summary report...')
summary_tracker.send_daily_summary()
print('✅ Daily summary completed')
