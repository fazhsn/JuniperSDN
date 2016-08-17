'''
Author - Faisal
Retrieve Links of the network
'''

import requests
requests.packages.urllib3.disable_warnings()
import json
from LabelPaths import LspDetail
from LSPProposerties import *
#from LinkEvent import LinkEvent

def Topology():
	url = "https://10.10.2.29:8443/oauth2/token"
	payload = {'grant_type': 'password', 'username': 'group1', 'password': 'Group1'}
	response = requests.post (url, data=payload, auth=('group1','Group1'), verify=False)
	json_data = json.loads(response.text)
	authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}
	r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1', headers=authHeader, verify=False)
	Topology = json.loads(r.text)
	#print Topology	
	return Topology

def GetLink():
	url = "https://10.10.2.29:8443/oauth2/token"
	payload = {'grant_type': 'password', 'username': 'group1', 'password': 'Group1'}
	response = requests.post (url, data=payload, auth=('group1','Group1'), verify=False)
	json_data = json.loads(response.text)
	authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}
	#print "GetLinks before get"
	r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/links', headers=authHeader, verify=False)
	LinksDict = json.loads(r.text)
	#print LinksDict	
	return LinksDict
	
def GetNodes():
	url = "https://10.10.2.29:8443/oauth2/token"
	payload = {'grant_type': 'password', 'username': 'group1', 'password': 'Group1'}
	response = requests.post (url, data=payload, auth=('group1','Group1'), verify=False)
	json_data = json.loads(response.text)
	authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}
	r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/nodes', headers=authHeader, verify=False)
	#NodesDict = json.loads(r.text)
	NodesCmplxDict=	json.loads(r.text)
	#print NodesDict	
	return NodesCmplxDict

def getNodesDict():
	NodesCmplxDict = GetNodes()
	nodes = {}
	for node in NodesCmplxDict:
		nodes[node['hostName']] = node['name']
	return nodes
'''
def getReverNodesDic():
	NodesCmplxDict = GetNodes()
	nodes = {}
	for node in NodesCmplxDict:
		nodes[node['name']] = node['hostName']
	return nodes
'''
# The objective of this Function is to Search The Failed link in the LSP Paths and Trigger a notification to PathRecoveryModule

def SearchLink(IP,LSP):
	Found = False
	for eachEro in LSP.ero:
		eroip = eachEro
		eroipUp = eroip[:-1]+'1'
		eroipdown = eroip[:-1]+'2'
		if IP == eachEro or IP == eachEro[:-1]+'1':
			#print LSP.SRLG
			Found = True

	return Found

# Need this Function To Be Generalized
def createLSPClass():
	bw = '1000'
	latency = '2'
	throughput = '1'
	ero=[]
	LSP1=LSPPath("GROUP_ONE_SF_NY_LSP1",bw,latency,throughput,ero)
	LSP2=LSPPath("GROUP_ONE_SF_NY_LSP2",bw,latency,throughput,ero)
	LSP3=LSPPath("GROUP_ONE_SF_NY_LSP3",bw,latency,throughput,ero)
	LSP4=LSPPath("GROUP_ONE_SF_NY_LSP4",bw,latency,throughput,ero)
	return LSP1,LSP2,LSP3,LSP4

#for testing run this 
def PopulateEro(LSP1,LSP2,LSP3,LSP4):
	n=0
	url = "https://10.10.2.29:8443/oauth2/token"
	payload = {'grant_type': 'password', 'username': 'group1', 'password': 'Group1'}
	response = requests.post (url, data=payload, auth=('group1','Group1'), verify=False)
	json_data = json.loads(response.text)
	authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}
	while n< 4:	
		#raw_input('Enter to continue')
		if n==0 and LSP1.LSPName.find("LSP1") != -1:
			lsp = LSP1.LSPName
			Rlsp = 'GROUP_ONE_NY_SF_LSP1'
			new_lsp = LspDetail(authHeader,lsp)
			new_Rlsp = LspDetail(authHeader,Rlsp)
			PopulateEROappend(new_lsp,new_Rlsp,LSP1)
			#SearchLink(LSP1)
			#displaypiero(LSP1)
			n= n+1
		elif n==1 and LSP2.LSPName.find("LSP2") != -1:
			lsp = LSP2.LSPName
			Rlsp = 'GROUP_ONE_NY_SF_LSP2'
			new_lsp = LspDetail(authHeader,lsp)
			new_Rlsp = LspDetail(authHeader,Rlsp)
			PopulateEROappend(new_lsp,new_Rlsp,LSP2)
			#SearchLink(LSP2)
			#displaypiero(LSP2)
			n=n+1
		elif n==2 and LSP3.LSPName.find("LSP3") != -1:
			lsp = LSP3.LSPName
			Rlsp = 'GROUP_ONE_NY_SF_LSP3'
			new_lsp = LspDetail(authHeader,lsp)
			new_Rlsp = LspDetail(authHeader,Rlsp)
			PopulateEROappend(new_lsp,new_Rlsp,LSP3)
			#SearchLink(LSP3)			
			#displaypiero(LSP3)
			n=n+1
		elif n==3 and LSP4.LSPName.find("LSP4") != -1:
			lsp = LSP4.LSPName
			Rlsp = 'GROUP_ONE_NY_SF_LSP4'
			new_lsp = LspDetail(authHeader,lsp)
			new_Rlsp = LspDetail(authHeader,Rlsp)
			PopulateEROappend(new_lsp,new_Rlsp,LSP4)
			#SearchLink(LSP4)			
			#displaypiero(LSP4)
			n=n+1
		else:
			break
			print "no more"
		
	#LSP.displayERO()



def PopulateEROappend(new_lsp,new_Rlsp,LSP):
	#LSP.ResetERO()
	LinkIP = '10.210' # slight Hard coded to eliminate extra address from the lists
	#print new_lsp
	for ad in new_lsp['plannedProperties']['ero']:
		if ad['address'].find(LinkIP)!=-1:
			LSP.CurrentERO(ad['address'])
	#print '----'
	#	print new_Rlsp['plannedProperties']['ero']
	#print '----'
	'''for ad in new_Rlsp['plannedProperties']['ero']:
		if ad['address'].find(LinkIP) != -1:
			LSP.RCurrentERO(ad['address'])
	'''		


def LinkToERO(lid):
	ero = lid.split('_')[0][1:]
	rero = lid.split('_')[1]
	print ero
	print rero
	return ero,rero

def displaypiero(LSP):
	LSP.displayERO()
	#LSP2.displayERO()
	#LSP3.displayERO()



#PopulateEro()
'''
L1,L2,L3,L4 = createLSPClass()
PopulateEro(L1,L2,L3,L4)
displaypiero(L1)


def FindLatency():


SearchLink()
'''



