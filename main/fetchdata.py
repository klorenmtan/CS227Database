fileReader = open("../data/sample.csv","r")

for line in fileReader:
	line=line[:-1]
	print(line)
fileReader.close()
