
import redis
import json
#import time
from LinkAPI import GetNodes, GetLink,getNodesDict
from collections import defaultdict
from LinkObj import Link
#nodes= {}


def IPtoNodeName(NodeIP,nodesdict):
	'''nodes = GetNodes()
	print "nodes printed"
	for node in nodes :
		if NodeIP == node['name']:
			srcName = node['hostName']
	return srcName'''
	for key in nodesdict.keys():
		if nodesdict[key] == NodeIP :
			srcName = key
	return srcName
#Call the below function after you call the above function
def latencydef(src,dst):
	#print dst
	if dst =='LA' :
		dst = 'los angeles'
	if src =='LA' :
		src = 'los angeles'
	srclower = src.lower()
	dstlower = dst.lower()
	if srclower =='sf' :
		srclower = 'san francisco'
	elif dstlower == 'sf' :
		dstlower = 'san francisco'
	elif srclower =='ny':
		srclower = 'new york'
	elif dstlower =='ny' :
		dstlower = 'new york'
	else :
		srclower = srclower
		dstlower = dstlower

	r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
	TrafficStats = r.lrange(srclower+':'+dstlower+':latency', 0, -1)[0]
	traffic = json.loads(TrafficStats)
	latency = traffic['rtt-average(ms)']
	return latency

def CurrentLinkUtil():
	#link =dict[("link"][('src','dst'))]
	LinkDict = {}
	links = GetLink()
	print "links printed"
	nodesdict = getNodesDict()
	for link in links:
		#LinkDict[link['name']] = [link['endA']['node']['name'],link['endA']['node']['name'],link['operationalStatus']]
		#print link['name']
		#print link['endA']['node']['name']
		#print link['endZ']['node']['name']
		#print link['operationalStatus']
		#print LinkDict
		srcIP = link['endA']['node']['name']
		dstIP = link['endZ']['node']['name']
		srcName = IPtoNodeName(link['endA']['node']['name'],nodesdict)
		dstName = IPtoNodeName(link['endZ']['node']['name'],nodesdict)
		linklatency = latencydef(srcName,dstName)
		#linkObj = Link(link['name'],srcIP,dstIP,srcName,dstName,linklatency
		linkobject = Link(link['name'],srcIP,dstIP,srcName,dstName,linklatency)
		LinkDict[link['name']] = linkobject		
	return LinkDict
 

'''
	#raw_input('Enter to continue')
	#for lId in LinkDict.keys():
		#print lId
		#print LinkDict[lId]
	#print LinkDict
	#print LinkDict['L10.210.11.1_10.210.11.2']
	#raw_input('Enter too continue')
	while True :
		#time.sleep(10)
		r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
		Keys = r.keys()
		total =0

		for key in Keys :
			if key.find(':latency') != -1 :
				TrafficStats = r.lrange(key, 0, -1)[0]
				traffic = json.loads(TrafficStats)
				traffic['to-router']
				traffic['from-router']
				print traffic['rtt-average(ms)']
				#raw_input('Thankyou')
				for each in traffic:
					print each
				
				#nodes = GetNodes()
				#links = GetLink()
				#for link in links
				
				Linkdict =  json.dumps(links)
				print Linkdict					
					#print links




 # decode json; convert json string to python dictionary
				#total = int(traffic['stats'][0]['input-bps'][0]['data'])
				#print key
				#print traffic 
			#print "The Network Status Needed Needs to be added "
			#print key
			#print total

'''
'''
linkDict = CurrentLinkUtil()
print linkDict	
for lid in linkDict.keys():	
	print "\t", linkDict[lid]#.srcIP
'''
