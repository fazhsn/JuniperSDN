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
	print "GetLinks before get"
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
	NodesDict = json.loads(r.text)
	#print NodesDict	
	return NodesCmplxDict

def getNodesDict():
	NodesCmplxDict = GetNodes()
	nodes = {}
	for node in NodesCmplxDict:
		nodes[node['hostName']] = node['name']
	return nodes

# The objective of this Function is to Search The Failed link in the LSP Paths and Trigger a notification to PathRecoveryModule

def SearchLink(IP,LSP):
	'''url = "https://10.10.2.29:8443/oauth2/token"
	payload = {'grant_type': 'password', 'username': 'group1', 'password': 'Group1'}
	response = requests.post (url, data=payload, auth=('group1','Group1'), verify=False)
	json_data = json.loads(response.text)
	authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}
	'''
	#ActiveLinks = GetLink()
	#print ActiveLinks
	#print LSP.SRLG
	#print LSP.ero
	Found = False
	for eachEro in LSP.ero:
			if IP == eachEro or IP == eachEro[:-1]+'1':
				print LSP.SRLG
				Found = True
			'''	
			if links ["name"].find(eachEro) != -1 :
				LSP.CompleteLink(links["name"])	
				#print LSP.upLink
				#print LSP.downLink
			#print links["name"]
			#raw_input('Enter to Continue')'''
	#print LSP.upLink
	return Found
	raw_input('Enter to Continue')

# Need this Function To Be Generalized
def createLSPClass():
	#Labels = ["GROUP_ONE_SF_NY_LSP1", "GROUP_ONE_SF_NY_LSP2","GROUP_ONE_SF_NY_LSP3","GROUP_ONE_SF_NY_LSP4","GROUP_ONE_NY_SF_LSP1","GROUP_ONE_NY_SF_LSP2","GROUP_ONE_NY_SF_LSP3","GROUP_ONE_NY_SF_LSP4"]
#for lsp in Labels:
	bw = '1000'
	latency = '2'
	throughput = '1'
	ero=[]
	LSP1=LSPPath("GROUP_ONE_SF_NY_LSP1",bw,latency,throughput,ero)
	LSP2=LSPPath("GROUP_ONE_SF_NY_LSP2",bw,latency,throughput,ero)
	LSP3=LSPPath("GROUP_ONE_SF_NY_LSP3",bw,latency,throughput,ero)
	LSP4=LSPPath("GROUP_ONE_SF_NY_LSP4",bw,latency,throughput,ero)
	#LSP5=LSPPath(LSPN1,bw,latency,throughput,ero)
		#LSP6=LSPPath(LSPN1,bw,latency,throughput,ero)
		#LSP7=LSPPath(LSPN1,bw,latency,throughput,ero)
		#LSP8=LSPPath(LSPN1,bw,latency,throughput,ero)
	return LSP1,LSP2,LSP3,LSP4 #,LSP5,LSP6,LSP7,LSP8


def PopulateEro(LSP1,LSP2,LSP3,LSP4):
	n=0
	url = "https://10.10.2.29:8443/oauth2/token"
	payload = {'grant_type': 'password', 'username': 'group1', 'password': 'Group1'}
	response = requests.post (url, data=payload, auth=('group1','Group1'), verify=False)
	json_data = json.loads(response.text)
	authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}
	#LSP1,LSP2,LSP3,LSP4 = createLSPClass() #,LSP5,LSP6,LSP7,LSP8 = createLSPClass(lsp)
	#print LSP1
	
	while n< 4:	
		#raw_input('Enter to continue')
		if n==0 and LSP1.LSPName.find("LSP1") != -1:
			lsp = LSP1.LSPName
			new_lsp = LspDetail(authHeader,lsp)
			PopulateEROappend(new_lsp,LSP1)
			#SearchLink(LSP1)
			#displaypiero(LSP1)
			n= n+1
		elif n==1 and LSP2.LSPName.find("LSP2") != -1:
			lsp = LSP2.LSPName
			new_lsp = LspDetail(authHeader,lsp)
			PopulateEROappend(new_lsp,LSP2)
			#SearchLink(LSP2)
			#displaypiero(LSP2)
			n=n+1
		elif n==2 and LSP3.LSPName.find("LSP3") != -1:
			lsp = LSP3.LSPName
			new_lsp = LspDetail(authHeader,lsp)
			PopulateEROappend(new_lsp,LSP3)
			#SearchLink(LSP3)			
			#displaypiero(LSP3)
			n=n+1
		elif n==3 and LSP4.LSPName.find("LSP4") != -1:
			lsp = LSP4.LSPName
			new_lsp = LspDetail(authHeader,lsp)
			PopulateEROappend(new_lsp,LSP4)
			#SearchLink(LSP4)			
			#displaypiero(LSP4)
			n=n+1
		else:
			break
			print "no more"
		
	#LSP.displayERO()



def PopulateEROappend(new_lsp,LSP):
	LinkIP = '10.210' # slight Hard coded to eliminate extra address from the lists
	for ad in new_lsp['plannedProperties']['ero']:
		if ad['address'].find(LinkIP)!=-1:
			#print ad['address']
			LSP.CurrentERO(ad['address'])



def displaypiero(LSP):
	LSP.displayERO()
	#LSP2.displayERO()
	#LSP3.displayERO()



#PopulateEro()

#createLSPClass()
#displaypiero()


'''
def FindLatency():


SearchLink()
'''



