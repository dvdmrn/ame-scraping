import csv

# REQUIRES: a .csv with recent games

print("hello")

with open('team_data.csv', newline='') as team_csv, open('games.csv', newline='') as games_csv:
    teamReader = csv.DictReader(team_csv)
    gameReader = csv.DictReader(games_csv)
    teamReader.next()
    gameReader.next()
    print("henlo")
