import csv



def main():

	complete_csv_of_users = 'user_data.csv'
	complete_csv_of_teams = 'team_data.csv'
	complete_csv_of_games = 'game_data.csv'

	teams = []
	games = []
	users = []

	with open(complete_csv_of_users, newline='') as users_csv, open(complete_csv_of_games, newline='') as games_csv, open(complete_csv_of_teams, newline='') as teams_csv:
	    userReader = csv.DictReader(users_csv)
	    teamReader = csv.DictReader(teams_csv)
	    gameReader = csv.DictReader(games_csv)
	    users = list(userReader)
	    teams = list(teamReader)
	    games = list(gameReader)
	    cleanUsers(users,games,teams)


# TODO: users must be associated with a team
def cleanUsers(users,games,teams):
	keepMe = []
	for user in users:
		print("evaluating user: ",user)
		for game in games:
			for team in teams:
				if game["TEAM ID"] in team["TeamID"]:
					# print("found team: ",team)
					



main()