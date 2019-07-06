# ame-scraping

## How to use

### Creating the comprehensive Users and Teams sheets: 
1. edit settings.json with the parameters of the pages you want to scrape
2. run by calling `python main.py`

### Creating the Games sheet:
1. Ensure you have created full Users and Teams sheets from the previous step
2. Download `games.csv` from the admin panel and place it in the root directory.
3. run by calling `python ProcessGames.py`

### Final steps: comprehensive user sheet and active users
1. Ensure that you have created: `game_data.csv`,`user_data.csv`,`team_data.csv`,`teamXuser-consent.csv`
2. Run by calling `python CreateUserSheets.py`
3. It should output `comprehensive_user_data.csv` and `active_users.csv`


### script flow

```
ScrapeProfiles.py -> populates scraped-profiles/ with .html docs
 |
ParseProfiles.py -> generates user_data.csv
 |
ScrapeTeams.py -> populates scraped-teams/ with .html docs
 |
ParseTeams.py -> generates team_data.csv
 |
PlayerTeamMatching.py -> generates teamXuser-consent.csv

```

I'll make this readme better if someone other than myself ever uses these scripts. Until next time ~* 