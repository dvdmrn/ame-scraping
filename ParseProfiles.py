import sys
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import csv
import tqdm


_RAW_PATH = "scraped-profiles"
files = [f for f in listdir(_RAW_PATH) if isfile(join(_RAW_PATH, f))]


headers = [
	"Id",
	"First name", 
	"Age",
	"Occupation",
	"Gender",
	"Works in Tech",
	"Email",
	"Consented to terms"
] 

toWrite = []

def makeList():
	print("reading profile data...")
	for f in tqdm.tqdm(files):
		file = open(_RAW_PATH+"/"+f,"r")
		soupme = file.read()
		soup = BeautifulSoup(soupme, "lxml")
		spans = soup.findAll("span")

		row = {} 
		for i in range(0,len(spans)):
			if spans[i].text:
				for header in headers:
					# print("comapring: ",spans[i].text, header)
					if spans[i].text == header:
						# print("successful comparison: ",spans[i].text, header)
						row[header] = spans[i+1].text


		# look for an email
		anchors = soup.findAll("a", href=True)

		for a in anchors:
			if("@" in a.text):
				row["Email"] = a.text

		# print (row)
		toWrite.append(row)
		file.close()

def writeCSV():
	print("\n\n✏️ writing to user_data.csv...\n\n")
	with open("user_data.csv","w",newline='') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=headers)
		writer.writeheader()
		writer.writerows(toWrite)
	print("complete!")

def main():
	makeList()
	writeCSV()