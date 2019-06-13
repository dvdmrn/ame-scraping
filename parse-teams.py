import sys
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import csv
import helpers


_RAW_PATH = "scraped-teams"
_HEADERS = ["TeamID","players","opt-in"]



def findUserIDs(soup):
	userIDmap = {}
	# find userIDs
	# returns: dict
	for row in soup.findAll('table')[0].findAll('tr'):
		spans = row.findAll('span')
		try:
			int(spans[0].text)
			userIDmap[spans[1].text] = spans[0].text
		except:
			pass
	print("users & id:",userIDmap)
	return userIDmap

def findOptinNames(soup):
	# find opt-in names
	# returns: list
	optinNames = []
	labels = soup.findAll('label')
	for l in labels:
		if "optin-" in l.text:
			optinNames.append(l.parent.findNext("span").findNext("span").text)

	print("optins:", optinNames)
	return optinNames

def getOptinIDs(names,nmap):
	# gets IDs of ppl who've opted in
	# returns: list
	optinIDs=[]
	for name in names:
		if name in nmap:
			optinIDs.append(nmap[name])

	print("IDs of optins: ",optinIDs)
	return optinIDs

def writeCSV(toWrite):
	print("writing to team_data.csv...")
	with open("team_data.csv","w",newline='') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=_HEADERS)
		writer.writeheader()
		writer.writerows(toWrite)
	print("complete!")

def main():

	toWrite = []
	
	files = [f for f in listdir(_RAW_PATH) if isfile(join(_RAW_PATH, f))]
	# ASSUME: all files end in .html
	for file in files:
		print([f[:-5] for f in files])
		row = {}
		teamID = file[:-5]
		file = open(_RAW_PATH+"/"+file,"r")
		soupme = file.read()
		soup = BeautifulSoup(soupme, "lxml")
		userIDmap = findUserIDs(soup) # dict
		optinNames = findOptinNames(soup) # list
		optins = getOptinIDs(optinNames, userIDmap) # list
		row[_HEADERS[0]] = teamID # team id
		row[_HEADERS[1]] = userIDmap # players on team
		row[_HEADERS[2]] = optins # optins for team
		toWrite.append(row)
	writeCSV(toWrite)







main()
