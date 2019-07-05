import csv

def main():
	print("cross ref. users and teams...")
	_HEADERS = [
				"UserID",
				"TeamID",
				"optin"
			   ]

	toWrite = []

	with open('team_data.csv', newline='') as team_csv, open('user_data.csv', newline='') as user_csv:
		team_reader = csv.DictReader(team_csv)
		user_reader = csv.DictReader(user_csv)
		team_data = list(team_reader) # so we can iterate >1x
		for user in user_reader:
			row = {}
			row["UserID"] = user["Id"]
			row["TeamID"] = ""
			row["optin"] = "n"

			for team in team_data:
				if user["Id"] in team["players"]:
					print("Found match of ",user["Id"],"in",team["players"])
					row["TeamID"] = team["TeamID"]
					if user["Id"] in team["opt-in"]:
						print("And: ",user["Id"],"opted in!")
						row["optin"] = "y"
					else:
						row["optin"] = "n"
			toWrite.append(row)

	# write CSV ================================================

	with open("teamXuser-consent.csv","w",newline='') as csvFile:
			print("writing: teamXuser-consent.csv")
			writer = csv.DictWriter(csvFile, fieldnames=_HEADERS)
			writer.writeheader()
			writer.writerows(toWrite)

	print("complete!")