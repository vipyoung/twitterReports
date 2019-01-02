"""
This script extract the daily most frequent K hashtags and print them in a format that we can use in the html page which displays them.
Author: Sofiane Abbar

You can run the code as follows: python generate_cloud_data.py tweets.txt 50

"""

from collections import Counter, defaultdict
import json
import time
import sys


def to_ts_day(tw_time):
    return time.strftime('%Y-%m-%d', time.strptime(tw_time,'%a %b %d %H:%M:%S +0000 %Y'))

def generate_daily_hashatags(fname, topK=50):
    day_tags = defaultdict(list)
    with open(fname) as f:
	for line in f:
	    try:
                o = json.loads(line)
                day_tags[to_ts_day(o['created_at'])] += [x["text"] for x in o['entities']["hashtags"]]
	    except:
		continue

    for day in sorted(day_tags):
        print '===================', day
        for k, v in Counter(day_tags[day]).most_common(topK):
            print '{text: "%s", weight: %s},' % (k,v)


if __name__ == '__main__':
    try:
        fname = sys.argv[1]
        topK = int(sys.argv[2])
    except:
        print 'You need to provide path to data file and number of hashtags per day. E.g., python generate_cloud_data.py tweets.txt 50'
        sys.exit()
    generate_daily_hashatags(fname, topK)

