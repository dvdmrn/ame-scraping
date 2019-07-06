# ame-scraping

## How to use

### Creating the comprehensive Users and Teams sheets: 
1. edit settings.json with the parameters of the pages you want to scrape
2. run by calling `python main.py()`

### Creating the Games sheet:
1. Ensure you have created full Users and Teams sheets from the previous step

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