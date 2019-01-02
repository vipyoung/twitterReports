"""
This script generate time series of tweet volumes per hour or per day. 
Author: Sofiane Abbar

Run: python volume.py tweets.txt daily
"""

import time
from datetime import datetime
import json
from collections import defaultdict
import sys

try:
    fname = sys.argv[1]
    granularity = sys.argv[2]
except: 
    print "Provide path to data file and granularity (hourly or daily). Eg. python volume.py tweets.txt daily"
    sys.exit()

def to_ts(tw_time):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tw_time,'%a %b %d %H:%M:%S +0000 %Y'))

def to_ts_h(tw_time):
	return time.strftime('%Y-%m-%d %H', time.strptime(tw_time,'%a %b %d %H:%M:%S +0000 %Y'))

def to_ts_day(tw_time):
	return time.strftime('%Y-%m-%d', time.strptime(tw_time,'%a %b %d %H:%M:%S +0000 %Y'))


h_ts = defaultdict(int)
if granularity == 'hourly':
    funct = to_ts_h
else:
    # default is daily
    funct = to_ts_day

with open(fname) as f:
	for line in f:
		try:
			o = json.loads(line)
			h_ts[funct(o['created_at'])] += 1
		except:
			continue

for k in sorted(h_ts.keys()):
	print '%s,%s' % (k, h_ts[k])

