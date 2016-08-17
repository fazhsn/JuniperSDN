import redis
import json
import pprint
#from LabelPaths import LspDetail
from AuthClass import *
from LinkAPI import Topology , GetLink , GetNodes , SearchLink , createLSPClass , PopulateEro ,displaypiero, PopulateEROappend
#from LinkAPI import *
from backup import reroute
from route_engine import get_alt_path
from LabelPaths import LabelModify,LspDetail
from LatencyListen import CurrentLinkUtil
#Labels List
def LinkEvent():
	head = Auth()
	header = head.Authheader()
	#Authentication
	auth = Auth()
	header= auth.Authheader()
	r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
	pubsub = r.pubsub()
	pubsub.subscribe('link_event')
	print "\n\n"
	print "___"	
	#print r.keys()
	AffectedLSPlist = []
	linkDict = CurrentLinkUtil()
	LSP1,LSP2,LSP3,LSP4 = createLSPClass()
	PopulateEro(LSP1,LSP2,LSP3,LSP4)
	F1 =False
	F2 =False
	F3= False
	F4 = False
	it = {"status": "failed", "router_id": "10.210.10.112", "timestamp": "Mon:00:37:44", "interface_address": "10.210.18.1", "interface_name": "ge-1/0/4", "router_name": "miami"}
	while True:
		#for item in pubsub.listen():
	    #LSP1,LSP2,LSP3,LSP4 = createLSPClass()
	    	#PopulateEro(LSP1,LSP2,LSP3,LSP4)
	   # F1,F2,F3,F4 = False
	    #print item['channel'], ":", item['data']
	    	item = it
	    #if isinstance(item['data'], basestring):
	        #d = json.loads(item)
		d= item
		print "\n\n"
		print "____________"
		print d['interface_address']
		n=0
		print d['status']
		if d['status'] == 'failed':
			print 'inside if loop'
			print n
			while n<4:
				if n == 0:
					print LSP1.ero
					F1 = SearchLink(d['interface_address'],LSP1)
					n=n+1
					print F1
					print 'in F1'
					if F1 == True :
						print LSP1.ero
						AffectedLSPlist.append(LSP1)
					
				elif n == 1:
					print LSP2.ero
					F2 = SearchLink(d['interface_address'],LSP2)
					n=n+1

			                print F2
			                print 'in F2'
					if F2 == True :
						print LSP2.ero
						AffectedLSPlist.append(LSP2)
					#F2 = True
				
				elif n == 2:
					print LSP3.ero
					F3 = SearchLink(d['interface_address'],LSP3)
					n=n+1
			                print F3
			                print 'in F3'
					if F3 == True :
						AffectedLSPlist.append(LSP3)

					#F3 = True
				elif n == 3:
					print LSP4.ero
					F4 = SearchLink(d['interface_address'],LSP4)
					n=n+1
					print F4
					if F4 == True :
						AffectedLSPlist.append(LSP4)
					print 'in F4'


				else :
					break
		if F1 == True or F2 == True or F3 == True or F4 == True :
			from LinkAPI import LinkToERO
		 	lspList = ["GROUP_ONE_SF_NY_LSP1", "GROUP_ONE_NY_SF_LSP1"]
			pathDict = get_alt_path(lspList, d['interface_address'])
			#print pathDict
			for lsp in AffectedLSPlist:
				lsp.ResetERO()
			#lenth = len(AffectedLSPlist)
				print "Minimum Latency Paths"
				for key in pathDict.keys():
					if key == 1:
						print key
					#for delay in pathDict[indx].keys():
						for delay in pathDict[key].keys():
							for lid in pathDict[key][delay]:
								print lid
								if lsp.LSPName.find('')						
								rero,ero = LinkToERO(lid)
								lsp.CurrentERO(ero)
								lsp.RCurrentERO(rero)
				raw_input('Continue ...')
				print lsp.ero
				print lsp.Rero
				print lsp.LSPName
				fLSP = LspDetail(header,lsp.LSPName)				
				LabelModify(lsp.ero,fLSP)
				rLSP = LspDetail(header,lsp.RLSPName)
				LabelModify(lsp.Rero,rLSP)
							
				raw_input('Enter to continue')

		
	#return d['interface_address'],F1,F2,F3,F4		
		#pprint.pprint(d, width=1)


LinkEvent()
#print F2
