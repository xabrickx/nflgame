import nflgame


## Find the top 5 running backs by rushing yards in the first week of the 2017 season:
games = nflgame.games(2017, week=1)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(5):
    msg = '%s %d carries for %d yards and %d TDs'
    print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))

##Or you could find the top 5 passing plays in the same time period:
games = nflgame.games(2017, week=1)
plays = nflgame.combine_plays(games)
for p in plays.sort('passing_yds').limit(5):
    print(p)
