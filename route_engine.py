import requests
requests.packages.urllib3.disable_warnings()
import json
from shortestpaths import EppsteinShortestPathAlgorithm
import networkx as nx
from LatencyListen import CurrentLinkUtil
from LinkAPI import getNodesDict
from LinkObj import Link
from collections import defaultdict

maxEpPaths = 7
nToL = defaultdict(lambda:defaultdict(lambda:None))

def createTopologyGraph(nodes, links):
	graph = nx.DiGraph() # Directed Graph
	graph.add_node('s', name = "source", index= 's')
	graph.add_node('t', name = "destination",index='t')
	
	for nodeName in nodes.keys():
		print "nodeName = %s"%nodeName
		print "loopback = %s"%nodes[nodeName]
		graph.add_node(nodeName, name=nodeName, index=nodes[nodeName])
	edges = []
	for linkId in links.keys():
		linkObj = links[linkId]
		edges.append((linkObj.srcIP, linkObj.dstIP, linkObj.latency))
		edges.append((linkObj.dstIP, linkObj.srcIP, linkObj.latency))
		# self,lid,src,dst,srcName,dstName,latency
	graph.add_weighted_edges_from(edges)
	graph.add_edge('s', "SF", weight=0)
	graph.add_edge("NY", 't', weight=0)
	return graph

def get_alt_path(lspList, brknLink):
	nodes = getNodesDict()
	links = CurrentLinkUtil()
	for lid in links.keys():
		lnkObj = links[lid]
		nToL[lnkObj.srcName][lnkObj.dstName] = lid
	graph = createTopologyGraph(nodes, links)
	e=EppsteinShortestPathAlgorithm(graph)
	e._pre_process()
	counter=0
	altPath = []
	for delay, epPath in e.get_successive_shortest_paths():			# outputs minimum delay first 
		# maximum number of alternative paths to check
		counter+=1
		if counter==maxEpPaths:
			break
		for pre, cur in epPath:						# Finding path-bandwidth for each EpPath
			if pre is not 's' and cur is not 't':
				linkId = nToL[pre][cur]
				altPath.append(linkId)

	return altPath


def main():
	brknLink = "L_10.210.24.2_10.210.24.1"
	lspList = ["GROUP_ONE_SF_NY_LSP1", "GROUP_ONE_NY_SF_LSP1"]
    	altPath = get_alt_path(lspList, brknLink)
	print altPath


if __name__ == "__main__":
	main()
