import copy
from Metadata import *
class FileReader:
	def __init__(self,filename):
		self.filename   = filename
		self.dictValues = dict()
		self.keyList 	= []
		self.clean_data = {}
		data1=[]
	
	def fileRead(self,data):
		
		fileR = open(self.filename,"r")
		for line in fileR:
			line = line[:-1]
			data1 =line.split(",")
			data.append(list(data1))
		fileR.close()
		#print(data)
		self.data = data		
		#self.clean_data = Data(self.data,self.filename)

				

	def getData(self):
		return self.clean_data


	

	def printData(self,tblname):
		md = Metadata()
		self.no_columns = md.no_getColumns(tblname)
		#print (no_columns, type(no_columns))
		for i in range(0,len(self.data)):
			print (self.data[i][0])
			

