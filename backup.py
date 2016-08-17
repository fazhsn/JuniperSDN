
#from LinkEvent import LinkEvent
from AuthClass import *
from LabelPaths import *
def reroute(AffectedLinkIP, AffectedLSP):
	ero1_SRLG1 = ['10.210.18.2','10.210.20.2','10.210.25.2','10.210.26.1']
	#ero1_SRLG = ['10.210.18.2','10.210.18.2','10.210.18.2']
	head = Auth()
	header = head.Authheader()
	#raw_input('enter to continue')
	print AffectedLinkIP
	print AffectedLSP
	for lsp in AffectedLSP :
		#raw_input('enter to continue')
		if lsp.find('LSP1') !=-1  or lsp.find('LSP2') !=-1 or lsp.find('LSP3') !=-1  or lsp.find('LSP4') !=-1  :
			lspname = lsp
			print lspname
			lspfull = LspDetail(header,lspname)
			#raw_input('enter to continue')
			print lspfull
			#raw_input('enter')
			LabelModify(ero1_SRLG1,lspfull)
			print LspDetail(header,lspname)
	
		
			
	#firstIp = '10.210.18.2'


	#ero1_SRLG = []
	#ero1_SRLG =
	
#reroute('10.210.16.1',['LSP1'])
