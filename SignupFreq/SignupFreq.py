import sys
sys.path.insert(0, '../')
import helpers
import datetime as dt
from pprint import pprint 
import collections


def main():
	allUsers = helpers.openCSVdict("users.csv")

	userCount = 1
	lastDate = ""
	createdDates = [] 
	toWrite = [] # [{date:xxx-xx-xx,userDensity:n}, ...]

	[createdDates.append(u["created"][:10]) for u in allUsers]

	collections.Counter(createdDates)


	freq = collections.Counter(createdDates)

	allFreq = smoothDates(freq)

	# for k in freq.keys():
	# 	toWrite.append({"date":k,"freq":freq[k]})
	# pprint(toWrite)

	# helpers.writeCSV(toWrite,"signupFreq.csv",["date","freq"])



# def date():
# 	date = dt.datetime(2019,2,28)
# 	print(f"{date:%Y-%m-%d}")
# 	date2 = date + dt.timedelta(days=1)
# 	print(f"{date2:%Y-%m-%d}")

# 	print(date == date2)

# 	inputDT = dt.datetime.strptime("2019-05-26","%Y-%m-%d")
# 	print(inputDT)
# 	print(f"{inputDT:%Y-%m-%d}")
# 	inputDT += dt.timedelta(days=1)
# 	print(f"{inputDT:%Y-%m-%d}")

def gamesPerWk():
	allUsers = helpers.openCSVdict("pruned_games.csv")

	userCount = 1
	lastDate = ""
	createdDates = [] 
	toWrite = [] # [{date:xxx-xx-xx,userDensity:n}, ...]

	weeks = []
	[createdDates.append(u["DATE"][:10]) for u in allUsers]
	for d in createdDates:
		print("checking: ",d)
		weeks.append(dt.datetime.strptime(d,"%Y-%m-%d").isocalendar())

	pprint(weeks)

	# dd=collections.Counter(createdDates)


# gamesPerWk()
# main()

print(dt.datetime(2019,6,16).isocalendar())