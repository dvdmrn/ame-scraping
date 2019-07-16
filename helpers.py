import csv
import os

def openCSVdict(path):
	with open(path, newline='') as csv_file:
		dictReader = csv.DictReader(csv_file)
		dicts = list(dictReader)
		return dicts


def writeCSV(toWrite,filename,headers):
	print("\n\n✏️ writing to"+filename+"...\n\n")
	with open(filename,"w",newline='') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=headers)
		writer.writeheader()
		writer.writerows(toWrite)
	print("complete!")

def linearScanMissingFiles(minR,maxR,path):
	dirs = os.listdir(path)
	lostUsers = []
	for i in range(minR,maxR):
		found = False
		for d in dirs:	
			if str(i) in d:
				found=True
				break
		if not found:
			print("WARNING! NOT FOUND: ",i)
			lostUsers.append(str(i))

	with open("missing-"+path+".txt",'w') as file:
		file.write(str(lostUsers))
linearScanMissingFiles()