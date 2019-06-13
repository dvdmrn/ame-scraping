# ame-scraping

### script flow

```
scrape-admin.py -> populates scraped-profiles/ with .html docs
 |
parse-sites.py -> generates user_data.csv
 |
scrape-teams.py -> populates scraped-teams/ with .html docs
 |
parse-teams.py -> generates team_data.csv
 |
player-team-matching.py -> generates teamXuser-consent.csv

```

I'll make this readme better if someone other than myself ever uses these scripts. Until next time ~* 