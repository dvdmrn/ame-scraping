import csv
import numpy as np
import pprint as pp
import sys
sys.path.insert(0, '../')
import helpers

def getNumberOfGames(feedback):
	print("finding longest successive games")
	highestSoFar = 0
	for review in feedback:
		if len(review['SCNR'])-1 > highestSoFar: # we subtract 1 because we're throwing out the leading 0
			highestSoFar = len(review['SCNR'])
			print("found longest gamers:",highestSoFar)
	print("# of successive games:",highestSoFar)
	return highestSoFar

def makeContainer(n):
	c = {}
	for i in range(1,n+1):
		c[str(i)]=[]
	return c

def populateScores(kind,container,feedback):
	for review in feedback:
		for i in range(1,len(review[kind])):
			container[str(i)].append(review[kind][i])
	print("\n\n==========container: ",container)
	return container

def get_Ns(raw_scores):
	sampleSizes = {}
	for i in range(0,len(raw_scores)):
		sampleSizes["N_"+str(i+1)] = len(raw_scores[str(i+1)])
	print("sample sizes: ",sampleSizes)
	return sampleSizes

def get_averages(scores):
	d = {}
	for i in scores:
		float_scores = [float(n) for n in scores[i]]
		# print("scores: ",float_scores)
		# print("ave: ",np.average(float_scores))
		d[i] = np.average(float_scores)
	pp.pprint(d)
	return d

def shuffleScores(raw_scores):
	toWrite = []
	n = max([len(raw_scores[k]) for k in raw_scores])
	print("n: ",n)

	for i in range(0,n):
		row = {}
		for k in raw_scores:
			try:
				row[k] = raw_scores[k][i]
			except:
				row[k] = ""
		toWrite.append(row)
	return toWrite

def main():
	fdbk = []
	toWrite = [] # [{"1":k, "2":k,"3":k ...}]
	with open("../feedback_scores.csv",newline='') as fdbk_csv:
		    fdbkReader = csv.DictReader(fdbk_csv)
		    fdbk = list(fdbkReader)

	n_games = getNumberOfGames(fdbk)
	closenessScores = makeContainer(n_games)
	scenarioScores = makeContainer(n_games)
	clsn_raw = populateScores("CLSN",closenessScores,fdbk)
	scnr_raw = populateScores("SCNR",scenarioScores,fdbk)
	N = get_Ns(clsn_raw)
	print("---------------------\nave closeness: ")
	ave_clsn = get_averages(clsn_raw)
	print("---------------------\nave scenario: ")
	ave_scnr = get_averages(scnr_raw)
	print("clsn raw: ",clsn_raw)
	shiftedClsn = shuffleScores(clsn_raw)
	print("shifted clsns",shiftedClsn)
	shiftedScnr = shuffleScores(scnr_raw)

	HEADERS = ["1","2","3","4","5"]
	helpers.writeCSV(shiftedClsn,"closeness_raw.csv",HEADERS)
	helpers.writeCSV(shiftedScnr,"scenario_raw.csv",HEADERS)

main()