import csv
import pprint as pp
from tqdm import tqdm

def main():

	headers = ["ID","NAME","TEAM ID","EMAIL","OPT IN?","AGE","GENDER","TECH?","OCCUPATION"]

	complete_csv_of_users = 'user_data.csv'
	complete_csv_of_teams = 'team_data.csv'
	complete_csv_of_games = 'game_data.csv'
	userXteam_consent = 'teamXuser-consent.csv'

	teams = []
	games = []
	users = []

	with open(complete_csv_of_users, newline='') as users_csv, open(complete_csv_of_games, newline='') as games_csv, open(complete_csv_of_teams, newline='') as teams_csv, open(userXteam_consent, newline='') as userXteam_csv:
	    userReader = csv.DictReader(users_csv)
	    teamReader = csv.DictReader(teams_csv)
	    gameReader = csv.DictReader(games_csv)
	    userXteamReader = csv.DictReader(userXteam_csv)

	    users = list(userReader)
	    teams = list(teamReader)
	    games = list(gameReader)
	    userXteam = list(userXteamReader)

	    ss=createStandardSheet(users,userXteam,headers)
	    writeCSV(ss,"comprehensive_user_data.csv",headers)

	    activeUsers = activeUsersOnly(ss,games,headers)
	    writeCSV(activeUsers,"active_users.csv",headers)
	    # cleanUsers(users,games,teams)



def createStandardSheet(users,userXteam,headers):
	stdSheet = []
	print("creating comprehensive user sheet...")
	for user in tqdm(users):
		entry = {}
		for uXt in userXteam:
			if user["Id"] == uXt["UserID"]:
				entry[headers[0]] = user["Id"]
				entry[headers[1]] = user["First name"]
				entry[headers[2]] = uXt["TeamID"]
				entry[headers[3]] = user["Email"]
				entry[headers[4]] = uXt["optin"]
				entry[headers[5]] = user["Age"]
				entry[headers[6]] = user["Gender"]
				entry[headers[7]] = user["Works in Tech"]
				entry[headers[8]] = user["Occupation"]

				stdSheet.append(entry)


	return stdSheet

def writeCSV(toWrite,filename,headers):
	print("\n\n✏️ writing to"+filename+"...\n\n")
	with open(filename,"w",newline='') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=headers)
		writer.writeheader()
		writer.writerows(toWrite)
	print("complete!")

def activeUsersOnly(ss,games,headers):
	activeUsers = []
	print("findinga active users...")
	for user in tqdm(ss):
		for game in games:
			if user["TEAM ID"]==game["TEAM ID"]:
				activeUsers.append(user)
				break
	return activeUsers



main()

