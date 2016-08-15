import requests
requests.packages.urllib3.disable_warnings()
import json
from shortestpaths import EppsteinShortestPathAlgorithm
import networkx as nx



def createTopologyGraph():
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






def main():
    


if __name__ == "__main__":
main()
