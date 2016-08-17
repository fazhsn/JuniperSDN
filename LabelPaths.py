'''
Takes the Label_Name and Gives it details
@author: Faisal Heli Daniel
'''
import requests
requests.packages.urllib3.disable_warnings()
import json
from AuthClass import *

def LspDetail (authHeader, FindLSP):
	lastLsp ={}
	r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/', headers=authHeader, verify=False)
	p = json.dumps(r.json())
	lsp_list = json.loads(p)
	for lsp in lsp_list:
	    if lsp['name'] == FindLSP:
		break
	    else :
		lsp ={}
	return lsp

# LSPToModify is a LSP Dictionary got from the above def.. To call the below fucntion the above fucntion needs to be called.

def LabelModify(IPList,LspToModify):
# Fill only the required fields
	ero =[]
	for Ip in IPList:
		ero.append({'topoObjectType': 'ipv4', 'address': Ip})
	print ero

	new_lsp = {}
	for key in ('from', 'to', 'name', 'lspIndex', 'pathType'):
	    new_lsp[key] = LspToModify[key]


	new_lsp['plannedProperties'] = {
	    'ero': ero
	}
	head = Auth()
	header = head.Authheader()
	response = requests.put('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/' + str(new_lsp['lspIndex']), 
		                json = new_lsp, headers=header, verify=False)
	print response.text


'''
# For Testing 
IPList = ['10.210.16.2','10.210.17.1'] #,'10.210.11.2','10.210.12.2']
head = Auth()
header = head.Authheader()


FindLSP = 'GROUP_ONE_SF_NY_LSP1'
lsp =LspDetail(header,FindLSP)
print lsp
LabelModify(IPList,lsp)
'''
