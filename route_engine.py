import requests
requests.packages.urllib3.disable_warnings()
import json
from shortestpaths import EppsteinShortestPathAlgorithm
import networkx as nx
from LatencyListen import CurrentLinkUtil
from LinkAPI import getNodesDict
from LinkObj import Link

def get_nodes():
	nodesDict = {"1":

def createTopologyGraph(nodes, links):
	graph = nx.DiGraph() # Directed Graph
	graph.add_node('s', name = "source", index= 's')
	graph.add_node('t', name = "destination",index='t')
	
	for nodeIndx in nodes.keys():
		graph.add_node(nodeIndx, name=nodes[nodeIndx], index=nodeIndx)
	edges = []
	for linkId in links.keys():
		linkObj = links[linkId]
		edges.append((linkObj.src, linkObj.dst, linkObj.dly))
	graph.add_weighted_edges_from(edges)
	return graph

def get_alt_path(lspList, brknLink):
	nodes = getNodesDict()
	links = CurrentLinkUtil()
	graph = createTopologyGraph(nodes, links)


def main():
	brknLink = "L_10.210.24.2_10.210.24.1"
	lspList = ["GROUP_ONE_SF_NY_LSP1", "GROUP_ONE_NY_SF_LSP1"]
    	get_alt_path(lspList, brknLink)


if __name__ == "__main__":
main()
