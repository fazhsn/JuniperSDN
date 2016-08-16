import redis
import json
import pprint
#from LabelPaths import LspDetail
from AuthClass import *
from LinkAPI import Topology , GetLink , GetNodes , SearchLink , createLSPClass , PopulateEro , displaypiero , PopulateEROappend


#Labels List
def LinkEvent():
	#Authentication
	auth = Auth()
	header= auth.Authheader()
	r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
	pubsub = r.pubsub()
	pubsub.subscribe('link_event')
	print "\n\n"
	print "___"	
	print r.keys()
	LSP1,LSP2,LSP3,LSP4 = createLSPClass()
	PopulateEro(LSP1,LSP2,LSP3,LSP4)
	F1 =False
	F2 =False
	F3= False
	F4 = False
	for item in pubsub.listen():
	    #LSP1,LSP2,LSP3,LSP4 = createLSPClass()
	    PopulateEro(LSP1,LSP2,LSP3,LSP4)
	   # F1,F2,F3,F4 = False
	    #print item['channel'], ":", item['data']
	    if isinstance(item['data'], basestring):
		d = json.loads(item['data'])
		print "\n\n"
		print "____________"
		print d['interface_address']
		n=0
		while n<4:
			if n == 0:
				F1 = SearchLink(d['interface_address'],LSP1)
				n=n+1
				print F1
				print 'in F1'
				#F1 = True
			        				
			elif n == 1:
				F2 = SearchLink(d['interface_address'],LSP2)
				n=n+1

                                print F2
                                print 'in F2'

				#F2 = True
			        
			elif n == 2:
				F3 = SearchLink(d['interface_address'],LSP3)
				n=n+1
                                print F3
                                print 'in F3'

				#F3 = True
			elif n == 3:
				F4 = SearchLink(d['interface_address'],LSP4)
				n=n+1
				print F4
				print 'in F4'

			        return d['interface_address'],F1,F2,F3,F4
               			#pprint.pprint(d, width=1)

			else :
				break

	return d['interface_address'],F1,F2,F3,F4		
		#pprint.pprint(d, width=1)


IP,F1,F2,F3,F4 = LinkEvent()
#print F2