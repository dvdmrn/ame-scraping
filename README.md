# ame-scraping

## How to use

### Creating the basic Users, Teams and Feedback sheets: 
1. edit settings.json with the parameters of the pages you want to scrape
2. run by calling `python main.py`

### Creating the Games sheet:
1. Ensure you have created full Users and Teams sheets from the previous step
2. Download `games.csv` from the admin panel and place it in the root directory.
3. run by calling `python ProcessGames.py`

### Final steps: comprehensive users and active users sheets
1. Ensure that you have created: `game_data.csv`,`user_data.csv`,`team_data.csv`,`teamXuser-consent.csv`
2. Run by calling `python CreateUserSheets.py`
3. It should output `comprehensive_user_data.csv` and `active_users.csv`


#### general note: you should have a complete record of all users and teams in your scraped-{profiles/teams} directories to ensure that users, teams, and games are correctly matched.

### script outputs
An overview of each of the scripts and the files they output as well as their dependencies

```
main.py -> calls the following:

	ScrapeProfiles.py -> populates scraped-profiles/ with .html docs
	 |
	ParseProfiles.py -> generates user_data.csv
	[REQUIRES: scraped-profiles/*.html]
	 |
	ScrapeTeams.py -> populates scraped-teams/ with .html docs
	 |
	ParseTeams.py -> generates team_data.csv & feedback_scores.csv
	[REQUIRES: scraped-teams/*.html]
	 |
	PlayerTeamMatching.py -> generates teamXuser-consent.csv

ProcessGames.py -> generates game_data.csv
[REQUIRES: user_data.csv, team_data.csv, teamXuser-consent.csv, scraped-teams/*.html]

CreateUserSheets.py -> generates active_users.csv, comprehensive_user_data.csv
```