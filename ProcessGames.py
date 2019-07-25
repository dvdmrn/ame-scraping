import csv
import json
import pprint
# REQUIRES: a .csv with recent games

print("hello")

def main():
	complete_csv_of_users = 'user_data.csv'
	complete_csv_of_teams = 'team_data.csv'
	games_csv = 'games.csv'

	teams = []
	games = []
	users = []

	gameIDmapping = getIDMap()

	writeMeDaddy = []

	with open(complete_csv_of_users, newline='') as users_csv, open(games_csv, newline='') as games_csv, open(complete_csv_of_teams, newline='') as teams_csv:
	    userReader = csv.DictReader(users_csv)
	    teamReader = csv.DictReader(teams_csv)
	    gameReader = csv.DictReader(games_csv)
	    users = list(userReader)
	    teams = list(teamReader)
	    games = list(gameReader)

	for g in games:
		if not (g['time_taken'] == '') and not (g['scenario_id'] == '10'): # if elapsed time
			game = {}
			game["GAME ID"]=g['id']
			game["DATE"]=g['finished'][:10]
			game["CITY"]=gameIDmapping[g['scenario_id']][1]
			game["SCENARIO"]=gameIDmapping[g['scenario_id']][0]
			game["TEAM ID"]= g['team_id']
			game["TEAM NAME"]=getTeamName(g['team_id'],teams)
			game["MINS"] = g['time_taken']
			pprint.pprint(game)
			writeMeDaddy.append(game)

	writeCSV(writeMeDaddy)


def getTeamName(teamID,teams):
	for team in teams:
		if teamID == team["TeamID"]:
			return team["name"]

def getIDMap():
	gameIDfile = open("res/game-id-mappings.json")
	games = json.load(gameIDfile)
	gameIDfile.close()
	return games

def writeCSV(toWrite):
	print("\n\n✏️ writing to game_data.csv...\n\n")
	with open("game_data.csv","w",newline='') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=["GAME ID","DATE","CITY","SCENARIO","TEAM ID","TEAM NAME","MINS"])
		writer.writeheader()
		writer.writerows(toWrite)
	print("complete!")

# def ignoreMelbourne(games):
# 	for i in range(0,len(games)):
# 		if (games[i]["scenario_id"] == "10"):
# 			del
main()