import redis
import json
import time
from LinkAPI import *

class Link():
	#self.lid
	#self.src
	#self.dst
	#self.latency
	#self.bw
	#srcName=''
	#dstName=''
	def __init__(self,lid,src,dst,srcName,dstName,latency):
		self.lid = lid
		self.srcIP = src
		self.dstIP = dst
		self.srcName = srcName
		self.dstName = dstName
		self.latency = latency
	'''
	def IPtoNodeName(self,src):
		nodes = GetNodes()
		for node in nodes :
			if self.src == node['name']:
				self.srcName = node['hostname']

	def latencydef(self):
		r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
		Keys = r.keys()
		for key in keys:
			if key.find(self.srcName+':'+self.dstName+':latency') != -1 :
				TrafficStats = r.lrange(key, 0, -1)[0]
				traffic = json.loads(TrafficStats)
				self.latency = traffic['rtt-average(ms)']
'''
