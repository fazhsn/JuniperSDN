import requests
requests.packages.urllib3.disable_warnings()
import json
from shortestpaths import EppsteinShortestPathAlgorithm, draw_graph
import networkx as nx
from LatencyListen import CurrentLinkUtil
from LinkAPI import getNodesDict
from LinkObj import Link
from collections import defaultdict, OrderedDict

maxEpPaths = 30
nToL = defaultdict(lambda:defaultdict(lambda:None))

def createTopologyGraph(nodes, links):
	graph = nx.DiGraph() # Directed Graph
	#graph.add_node('s', name = "source", index= 's')
	#graph.add_node('t', name = "destination",index='t')
	
	for nodeName in nodes.keys():
		#print "nodeName = %s"%nodeName
		#print "loopback = %s"%nodes[nodeName]
		graph.add_node(nodeName, name=nodeName, index=nodeName)
	edges = []
	for linkId in links.keys():
		linkObj = links[linkId]
		#print "\tAdding Link %s --> %s with latency\t= %.4f"%(linkObj.srcName,linkObj.dstName, linkObj.latency)
		edges.append((linkObj.srcName, linkObj.dstName, linkObj.latency))
		#edges.append((linkObj.srcName, linkObj.dstName, 10))
		#print "\tAdding Link %s --> %s with latency\t= %.4f"%(linkObj.dstName, linkObj.srcName, linkObj.latency)
		edges.append((linkObj.dstName, linkObj.srcName, linkObj.latency))
		#edges.append((linkObj.dstName, linkObj.srcName, 10))
		# self,lid,src,dst,srcName,dstName,latency
	graph.add_weighted_edges_from(edges)
	#graph.add_edge('s', "SF", weight=0)
	#graph.add_edge("NY", 't', weight=0)
	#draw_graph(graph)
	return graph

def get_alt_path(brknLink):
	nodes = getNodesDict()
	links = CurrentLinkUtil()
	brknSrc = None
	brknDst = None
	#print "brknLink = %s"%brknLink
	for lid in links.keys():
		lnkObj = links[lid]
		nToL[lnkObj.srcName][lnkObj.dstName] = lid
		nToL[lnkObj.dstName][lnkObj.srcName] = lid
		#print "lid = %s"%lid
		if lid.find(brknLink) != -1:
			#print "getting src and dst of broknLink"
			brknSrc = lnkObj.srcName
			brknDst = lnkObj.dstName

	graph = createTopologyGraph(nodes, links)
	if brknSrc is not None and brknDst is not None:
		print "removing broken link  %s <--> %s "%(brknSrc, brknDst)
		graph.remove_edge(brknSrc, brknDst)
		graph.remove_edge(brknDst, brknSrc)

	e=EppsteinShortestPathAlgorithm(graph=graph, source='SF', destination='NY')
	e._pre_process()
	counter=0
	#pathDict = defaultdict(lambda:defaultdict(lambda:None))
	pathDict = {}
	keySet = set()
	pathNum = 1
	for delay, epPath in e.get_successive_shortest_paths():			# outputs minimum delay first 
		#pathLinks = []
		# maximum number of alternative paths to check
		counter+=1
		if counter>maxEpPaths:
			break
		strKey = ""
		for pre, cur in epPath:					
			strKey +=cur
			#linkId = nToL[pre][cur]
			#pathLinks.append(linkId)
			
		#pathDict[counter][delay] = pathLinks
		if strKey not in keySet:
			pathDict[pathNum] = epPath
			#pathDict[pathNum][delay] = epPath
			keySet.add(strKey)
			pathNum +=1

	return pathDict


def get_paths_for_lsps(lspList, brknLink):
    	pathDict = get_alt_path(brknLink)
	print "Minimum Latency Paths"
	#print"\tPath#\tDelay\tPath(From --> To)"
	for pthNum in pathDict.keys():
		for pre, cur in pathDict[pthNum]:
			print "\t%s-->%s"%(pre, cur),
		print
		#for delay in pathDict[pthNum].keys():
		#	print "\t%d\t%.4f"%(pthNum, delay),
		#	for pre, cur in pathDict[pthNum][delay]:
		#		print "\t%s-->%s"%(pre, cur),
		#	print

	#for lspObj in lspList:
		



def main():
	brknLink = "10.210.24.2"
#Refer LabelOBj for Deatils of Return type of LSP object
	lspList = ["GROUP_ONE_SF_NY_LSP1", "GROUP_ONE_NY_SF_LSP1"]
    	lspToPath = get_paths_for_lsps(lspList, brknLink)

if __name__ == "__main__":
	main()
