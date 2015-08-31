from Metadata import *
class Data:

	def __init__(self,tbldata,tblname):
		global md
		md=Metadata()		
		self.database={}
		self.tbldata = tbldata
		self.tblname = tblname
		self.clean_data = {}
		#self.datatypesArray=md.getAllDatatypes(self.tblname);
		#self.colNameArray = md.getAllColumns(self.tblname)
		self.getPrimary()
		self.addToHash()

	def getPrimary(self):
		self.primary_keys=[]
		#print (self.tblname)
		#print (md.no_getColumns(self.tblname))		
		for i in range (0,len(self.tbldata)):
			self.primary_keys.append((self.tbldata[i][0]))
		

	def addToHash(self):
		items1={}
		items2={}
		items={}
		columns=md.getAllColumns(self.tblname)
		datatype =md.getAllDatatypes(self.tblname)
		for i in range(1,len(datatype)):
			for j in range(0,len(self.tbldata)):	
				if datatype[i] == 'numeric':
					items1={columns[i]:float(self.tbldata[j][i])}
				if datatype[i] == 'int':
					items1={columns[i]:int(self.tbldata[j][i])}
				else:				
					items2={columns[i]:(self.tbldata[j][i])}
				items.update(items1)
				items.update(items2)				
				self.clean_data[self.primary_keys[j]]=items;			
				
	def getDataHash(self):
		return self.clean_data		

		


