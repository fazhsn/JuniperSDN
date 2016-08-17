
#from LinkEvent import LinkEvent
from AuthClass import *
from LabelPaths import *
def reroute(AffectedLinkIP, AffectedLSP):
	ero1_SRLG1 = ['10.210.18.2','10.210.20.2','10.210.25.2','10.210.26.1']
	#ero1_SRLG1 = []
	#ero1_SRLG = ['10.210.18.2','10.210.18.2','10.210.18.2']
	head = Auth()
	header = head.Authheader()
	#raw_input('enter to continue')
	print AffectedLinkIP
	print AffectedLSP
	for lsp in AffectedLSP :
		#raw_input('enter to continue')
		if lsp.LSPName.find('LSP1') !=-1  or lsp.LSPName.find('LSP2') !=-1 or lsp.LSPName.find('LSP3') !=-1  or lsp.LSPName.find('LSP4') !=-1  :
			lspname = lsp.LSPName
			Rlspname = lsp.RLSPName
			print "The following LSP are getting UPDATED"
			print lspname
			print Rlspname
			lspfull = LspDetail(header,lspname)
			Rlspfull = LspDetail(header,Rlspname)
			#raw_input('enter to continue')
			print lspfull
			#raw_input('enter')
			LabelModify(ero1_SRLG1,lspfull)
			LabelModify(ero1_SRLG1,Rlspfull)
			print LspDetail(header,Rlspname)
	
		
			
	#firstIp = '10.210.18.2'


	#ero1_SRLG = []
	#ero1_SRLG =
	
#reroute('10.210.16.1',['LSP1'])
