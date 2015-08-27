from Metadata import *
class Data:

	def __init__(self,tbldata,tblname):
		self.tbldata = tbldata
		self.tblname = tblname
		self.clean_data = {}
		self.datatypesArray=md.getAllDatatypes(self.tblname)	
		self.colNameArray = md.getAllColumns(self.tblname)

#	def getPrimaryKey(self,tbldata,tblname):
		

'''
	def convertDataTypes(self):
		for i in range (0,len(self.datatypesArray)):
			for j in range (0,len(self.tbldata)):
				for k in range (0,len(self.colNameArray)-1):
					self.clean_data[self.tbldata[j]]=append()
'''		
		
