"""
This script generate lists of most frequent users, hashtags, urls, mentions, etc. from a text in which each line is a json tweet.
Author: Sofiane Abbar

Run: python frequent_things.py data.txt
"""

from collections import Counter
import json
import sys

try:
    fname = sys.argv[1]
except:
    print 'You need to provide path to data file. E.g., python frequent_things.py tweets.txt'
    sys.exit()

lines = []
links = []
hashtags = []
mentions = []
users = []
locations = []
photos = []
ids = set()
cpt = 0
with open(fname) as f:
	for line in f:
		# try:
			o = json.loads(line)
			lines.append(o['full_text'])
			ids.add(o['id'])
			ws = [w.strip() for w in o['full_text'] if len(w.strip()) > 1]
			mentions += [x["screen_name"] for x in o['entities']["user_mentions"]]
			hashtags += [x["text"] for x in o['entities']["hashtags"]]
			links += [x["expanded_url"] for x in o['entities']["urls"]]
			if 'media' in o['entities']:
				photos += [x["media_url"] for x in o['entities']['media']]
			if o["user"]["screen_name"] not in users:
				locations.append(o["user"]["location"])
			users.append(o["user"]["screen_name"])
			cpt += 1
		# except:
			# continue
print cpt, len(ids)
lcnt = Counter(lines).most_common(1000)
hcnt = Counter(hashtags).most_common(1000)
mcnt = Counter(mentions).most_common(1000)
ucnt = Counter(links).most_common(1000)
uscnt = Counter(users).most_common(1000)
uloccnt = Counter(locations).most_common(1000)
pcnt = Counter(photos).most_common(1000)
with open('data/most_common_retweets.txt', 'w') as tg, open('data/most_common_hashtags.txt', 'w') as hg, \
		open('data/most_common_mentions.txt', 'w') as mg, open('data/most_common_links.txt', 'w') as ug, \
		open('data/most_common_users.txt', 'w') as usg, open('data/most_common_locations.txt', 'w') as ulocg,\
		open('data/most_common_photos.txt', 'w') as pg:
	for (k, v) in lcnt:
		tg.write('%s\t%s\n' % (v, k.encode('utf-8')))
	for (k, v) in hcnt:
		hg.write('%s\t%s\n' % (v, k.encode('utf-8')))
	for (k, v) in mcnt:
		mg.write('%s\t%s\n' % (v, k.encode('utf-8')))
	for (k, v) in ucnt:
		ug.write('%s\t%s\n' % (v, k.encode('utf-8')))
	for (k, v) in uscnt:
		usg.write('%s\t%s\n' % (v, k.encode('utf-8')))
	for (k, v) in uloccnt:
		ulocg.write('%s\t%s\n' % (v, k.encode('utf-8')))
	for (k, v) in pcnt:
		pg.write('%s\t%s\n' % (v, k.encode('utf-8')))

#
# # Clouds
# for k, v in hcnt:
#         print '{text: "%s", weight: %s},' % (k,v)
