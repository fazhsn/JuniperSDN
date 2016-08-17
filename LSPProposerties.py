'''
ERO lSP Paths 
Author Faisal
This is a standard Class which defines a LSP Path
'''

class LSPPath():
	def __init__(self,Name,bandwidth,latency,throughput,ero):
		self.LSPName = Name
		self.RLSPName = 'GROUP_ONE_NY_SF_'+Name[-4:]
		#self.SRLG = False
		self.bandwidth =bandwidth
		self.latency =latency
		self.throughput = throughput
		#self.hops = hops
		#self.distance = distance
		self.ero=[]
		self.Rero=[]
		self.FullLink = ""
		#self.upLink=[]
		#self.downLink=[]
		P1 = 'LSP1'
		P2 = 'LSP2'
		if self.LSPName.find(P1) != -1:
			self.SRLG = True
		else :
			self.SRLG = False

	def CurrentERO(self,ero):
		self.ero.append(ero)
	
	def RCurrentERO(self,Rero):
		self.Rero.append(Rero)
		

	def displayERO(self):
		print self.ero
		print self.Rero
	'''
	def CompleteLink(self,Link):
		self.FullLink = Link
		updown= self.FullLink.split('_')
		self.upLink.append(updown[0][1:])
		self.downLink.append(updown[1])
	'''
	def ResetERO(self):
		self.ero = []
		self.Rero = []
	
