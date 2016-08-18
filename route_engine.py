import requests
requests.packages.urllib3.disable_warnings()
import json
from shortestpaths import EppsteinShortestPathAlgorithm, draw_graph
import networkx as nx
from LatencyListen import CurrentLinkUtil
from LinkAPI import getNodesDict
from LinkObj import Link
from collections import defaultdict

maxEpPaths = 6
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
		edges.append((linkObj.srcName, linkObj.dstName, linkObj.latency))
		edges.append((linkObj.dstName, linkObj.srcName, linkObj.latency))
		#print "\tAdding Link %s --> %s"%(linkObj.srcName,linkObj.dstName)
		#edges.append((linkObj.srcName, linkObj.dstName, 10))
		#print "\tAdding Link %s --> %s"%(linkObj.dstName, linkObj.srcName)
		#edges.append((linkObj.dstName, linkObj.srcName, 10))
		# self,lid,src,dst,srcName,dstName,latency
	graph.add_weighted_edges_from(edges)
	#graph.add_edge('s', "SF", weight=0)
	#graph.add_edge("NY", 't', weight=0)
	#draw_graph(graph)
	return graph

def get_alt_path(lspList, brknLink):
	nodes = getNodesDict()
	links = CurrentLinkUtil()
	brknSrc = None
	brknDst = None
	print "brknLink = %s"%brknLink
	for lid in links.keys():
		lnkObj = links[lid]
		nToL[lnkObj.srcName][lnkObj.dstName] = lid
		nToL[lnkObj.dstName][lnkObj.srcName] = lid
		print "lid = %s"%lid
		if lid.find(brknLink) != -1:
			print "getting src and dst of broknLink"
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
	for delay, epPath in e.get_successive_shortest_paths():			# outputs minimum delay first 
		pathLinks = []
		# maximum number of alternative paths to check
		counter+=1
		if counter>maxEpPaths:
			break
		for pre, cur in epPath:						# Finding path-bandwidth for each EpPath
			if pre is not 's' and cur is not 't':
				linkId = nToL[pre][cur]
				pathLinks.append(linkId)
			
		#pathDict[counter][delay] = pathLinks
		pathDict[counter] = epPath

	return pathDict


def main():
	brknLink = "10.210.24.2"
#Refer LabelOBj for Deatils of Return type of LSP object
	lspList = ["GROUP_ONE_SF_NY_LSP1", "GROUP_ONE_NY_SF_LSP1"]
    	pathDict = get_alt_path(lspList, brknLink)
	print "Minimum Latency Paths"
	for indx in pathDict.keys():
		#for delay in pathDict[indx].keys():
		#	print "%d\t%.4f\t%s"%(indx, delay, pathDict[indx][delay])
		print "\t%d"%indx,
		for pre, cur in pathDict[indx]:
			print "\t%s-->%s"%(pre, cur),
		print


if __name__ == "__main__":
	main()
