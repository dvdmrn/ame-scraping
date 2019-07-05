import os
import sys
import json
import ScrapeProfiles
import ScrapeTeams
import ParseProfiles, ParseTeams
import PlayerTeamMatching

def setup_directories():
	if not os.path.isdir("./scraped-profiles"):
		print("⚠️ creating directory: scraped-profiles")
		os.mkdir("scraped-profiles")

	if not os.path.isdir("./scraped-teams"):
		print("⚠️ creating directory: scraped-teams")
		os.mkdir("scraped-teams")

def get_settings():
	print("\n\nlet's get scraping ;)")
	
	if not os.path.isfile("settings.json"):
		print("💀 cannot find settings.json!")
		sys.exit()
	
	settingsFile = open("settings.json")
	settings = json.load(settingsFile)
	settingsFile.close()

	if len(settings["login"]) < 30:
		print("💀 your login url doesn't look quite right")
		print("    - current login url:",settings["login"])
		sys.exit()

	return settings

def main():
	settings = get_settings()
	print("🔥 accessing with login credentials:",settings["login"])

	# get profile data and make csv
	ScrapeProfiles.main(settings)
	ParseProfiles.main()

	# get team data and make csv
	ScrapeTeams.main(settings)
	ParseTeams.main()

	# cross ref player x team data and make csv	
	PlayerTeamMatching.main()
	print("\n\nall done! Have a nice day 🌈")

main()