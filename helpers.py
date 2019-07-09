import csv

def writeCSV(toWrite,filename,headers):
	print("\n\n✏️ writing to"+filename+"...\n\n")
	with open(filename,"w",newline='') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=headers)
		writer.writeheader()
		writer.writerows(toWrite)
	print("complete!")
