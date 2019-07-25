import sys
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import csv
import tqdm

_RAW_PATH = "scraped-teams"
_HEADERS = ["TeamID","players","opt-in","name"]

noIDfound = []

def findUserIDs(soup,file):
	global noIDfound
	userIDmap = {}
	# find userIDs
	# returns: dict
	try:
		for row in soup.findAll('table')[0].findAll('tr'):
			spans = row.findAll('span')
			try:
				int(spans[0].text)
				userIDmap[spans[1].text] = spans[0].text
			except:
				pass
	except:
		noIDfound.append(file.name)
	# print("users & id:",userIDmap)
	return userIDmap

def findOptinNames(soup):
	# find opt-in names
	# returns: list
	optinNames = []
	labels = soup.findAll('label')
	for l in labels:
		if "optin-" in l.text:
			optinNames.append(l.parent.findNext("span").findNext("span").text)

	# print("optins:", optinNames)
	return optinNames



def getOptinIDs(names,nmap):
	# gets IDs of ppl who've opted in
	# returns: list
	optinIDs=[]
	for name in names:
		if name in nmap:
			optinIDs.append(nmap[name])

	# print("IDs of optins: ",optinIDs)
	return optinIDs

def writeCSV(toWrite,name,headers):
	print("\n\n✏️ writing to"+name+"...\n\n")
	with open(name,"w",newline='') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=headers)
		writer.writeheader()
		writer.writerows(toWrite)
	print("complete!")

def getTeamName(soup):
	labels = soup.findAll('label')
	name = ""
	for l in labels:
		if "Name" in l.text:
			name = l.parent.findNext("div").findNext("span").text
			return name

def getFdbk(soup,feedback):
	labels = soup.findAll('label')
	for l in labels:
		if "scenario-feedback" in l.text:
			feedbackScore = l.parent.findNext("div").findNext("span").text
			feedback["SCNR"].append(feedbackScore)
		if "closeness-feedback" in l.text:
			feedbackScore = l.parent.findNext("div").findNext("span").text
			feedback["CLSN"].append(feedbackScore)

def sortFeedbackScores(scores):
	output = []
	for i in range(0,max(len(scores["SCNR"]),len(scores["CLSN"]))):
		try:
			output.append({"SCNR":scores["SCNR"][i],"CLSN":scores["CLSN"][i]})
		except:
			if i > (len(scores["SCNR"])-1):
				output.append({"SCNR":"","CLSN":scores["CLSN"][i]})
			elif i > (len(scores["CLSN"])-1):
				output.append({"SCNR":scores["SCNR"][i],"CLSN":""})

	return output

def main():
	global noIDfound
	toWrite = []
	fdbk = {"SCNR":[],"CLSN":[]}
	
	files = [f for f in listdir(_RAW_PATH) if isfile(join(_RAW_PATH, f))]
	# ASSUME: all files end in .html


	for file in tqdm.tqdm(files):
		# print([f[:-5] for f in files])
		# print("accessing: "+file)
		row = {}
		teamID = file[:-5]
		file = open(_RAW_PATH+"/"+file,"r")
		soupme = file.read()
		soup = BeautifulSoup(soupme, "lxml")
		userIDmap = findUserIDs(soup,file) # dict
		optinNames = findOptinNames(soup) # list
		optins = getOptinIDs(optinNames, userIDmap) # list
		teamName = getTeamName(soup)
		feedbackScores = getFdbk(soup,fdbk)
		row[_HEADERS[0]] = teamID # team id
		row[_HEADERS[3]] = teamName # team name
		row[_HEADERS[1]] = userIDmap # players on team
		row[_HEADERS[2]] = optins # optins for team
		toWrite.append(row)
	
	if(noIDfound):
		print("\n\n\n⚠️ ⚠️ ⚠️\nWARNING:\n🤔 I CANNOT FIND USER IDs IN THE FOLLOWING FILES: ",noIDfound,"\n\n\n")
	writeFeedbackScores = sortFeedbackScores(fdbk) # reformats so that scores are writable
	writeCSV(toWrite,"team_data.csv",_HEADERS)
	writeCSV(writeFeedbackScores,"feedback_scores.csv",["SCNR","CLSN"])