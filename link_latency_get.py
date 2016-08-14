'''
This Function givens the latency of a link and jitter
The jitter is calculated by using the formula
Jitter = (Max Latency - Avergare Latency)^2/2
Authors - Faisal, Daniel, Heli
Purpose - NorthStart COntroller Juniper SDN Throwdown
'''

import redis
import json
#import subprocess
#import os
import pprint
class RedisStatus:
	def __init__(self,src,dst,node,intf):
		self.src = src
		self.dst = dst
		self.node = node
		self.intf = intf
	def AvergaeLatency(self):
		r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
	# r.lrnage(src :dst:latency, from record, to record)[total number of records whose average needs to be taken]
		latency_avg = r.lrange(self.src+':'+self.dst+':latency', 0, 10)
		#print latency_avg
		if latency_avg :	
			latency_comp = r.lrange(self.src+':'+self.dst+':latency', 0, -1)[0]
		else :
			latency_comp = []
		#print latency_avg
		last_latency =[]
		if latency_avg:
			latency_recent = json.loads(latency_comp)

			for ea in latency_avg:
				latency_dict = json.loads(ea)
				last_latency.append(float(latency_dict['rtt-average(ms)']))	
		
			avglatency_final = float(latency_recent['rtt-average(ms)'])
			recentMax = max(last_latency)
		else :
			avglatency_final=0.0
			recentMax=0.0
			
		MeanJitter = ((recentMax-avglatency_final)**2)/2
		jitter = recentMax-avglatency_final
		print jitter



	def ErrorList(self):
		r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
		TrafficStats = r.lrange(self.node +':'+self.intf+':traffic statistics', 0, -1)
		if TrafficStats :
			TrafficStats = r.lrange(self.node +':'+self.intf+':traffic statistics', 0, -1)[0]
			print TrafficStats # json-formatted string
			print isinstance (TrafficStats, str)
			data = json.loads(TrafficStats) # decode json; convert json string to python dictionary
			print data
			print "The Network Status Needed Needs to be added "
			print data['stats'][0]['input-bps'][0]['data']
		else:
			print TrafficStats
			print "Check Interface/ HostName/InterfaceName"

