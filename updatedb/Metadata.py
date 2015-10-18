class Metadata:
	def __init__(self):
		self.metadatafile = 'config.txt'; 
		self.metaData = []
		self.ReadMetaData()

	def ReadMetaData(self):
		filer = open(self.metadatafile)
		for line in filer:
			line = line[:-1]
			data = line.split(",")
			(self.metaData).append(list(data))
		#print(self.metaData)
		filer.close()
		

	def showMetaData(self,tblname):
		columns = self.getAllColumns(tblname)
		datatypes = self.getAllDatatypes(tblname)
		printCOL = "COLUMNS"
		printDAT = "DATA TYPE"
		print ("%30s"%printCOL,"\t","%30s"%printDAT)
		for i in range(0,len(columns)):
			print ("%30s"%columns[i],"\t","%30s"%datatypes[i])

				
	
	def getAllTableName(self):
		tblNames=[]
		for i in range(0,len(self.metaData)):
			tblNames.append(self.metaData[i][0])
		return tblNames

	def no_getColumns(self,tblname):
		for i in range(0,len(self.metaData)):
			if self.metaData[i][0] == tblname:
				return int(self.metaData[i][1])
	
	def checkTableExist(self,tblname):
		tblNames=self.getAllTableName()
		for i in range(0,len(tblNames)):
			if tblNames[i] in tblname:
				return True
		return False
		

	def getAllColumns(self,tblname):
		columns=[]
		j=2
		for i in range(0,len(self.metaData)):
			if self.metaData[i][0] == tblname:
				for j in range(2,((self.no_getColumns(tblname))*2)+2,2):	
					columns.append(self.metaData[i][j])
		return columns


	def getAllDatatypes(self,tblname):
		datatypes=[]
		j=2
		for i in range(0,len(self.metaData)):
			if self.metaData[i][0] == tblname:
				for j in range(3,((self.no_getColumns(tblname))*2)+2,2):	
					datatypes.append(self.metaData[i][j])
		return datatypes

	def checkcolumnExist(self,tblname,colname):
		columns=self.getAllColumns(tblname)
		if self.checkTableExist(tblname):
			for i in range(0,len(self.getAllColumns(tblname))):
				if colname == columns[i]:
					return True
			return False 
		
				
