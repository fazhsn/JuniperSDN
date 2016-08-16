

import redis
import json
#import subprocess
#import os
#import pprint


def CurrentLinkUtil():
	r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
	Keys = r.keys()
	total =0
	for key in Keys :
		if key.find(':traffic statistics') != -1 :
			TrafficStats = r.lrange(key, 0, -1)[0]
			traffic = json.loads(TrafficStats) # decode json; convert json string to python dictionary
			total = int(traffic['stats'][0]['input-bps'][0]['data'])
			print "The Network Status Needed Needs to be added "
			print key
			print total


CurrentLinkUtil()		
	

