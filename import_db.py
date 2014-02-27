import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mm-db']


##import stats
collection = db['team-stats']
team_stats = db['team-stats'].remove() ##did this so it doesn't keep appending if you rerun it
team_stats = db['team-stats']

stats_file = open('stats.txt')
stats_lines = stats_file.readlines()

mapping = ['Team Name', 'Total Games', 'Wins', 'Losses', 'Winning Pct', 'Possessions', 'Possessions Per 40 minutes', 'Floor Pct', 'Efficiency', 'Field Goals Made', 'Field Goal Attempts', 'Field Goal Pct', 'Free Throws Made', 'Free Throw Attempts', 'Free Throw Pct', '3-pt Field Goals Made', '3-pt Field Goal Attempts', '3-pt Field Goal Pct', 'Effective Field Goal Pct', 'True Shooting Pct', 'Free Throw Rate', 'Field Goal Point Pct', 'Free Throw Point Pct', '3-pt Field Goal Point Pct', 'Points Per Possessions', 'Points', 'Points Per Game', 'Rebound Pct', 'Total Rebounds', 'Total Rebounds Per Game', 'Offensive Reb Pct', 'Offensive Rebounds', 'Offensive Rebounds Per Game', 'Defensive Reb Pct', 'Defensive Rebounds', 'Defensive Rebounds Per Game', 'Team Rebounds', 'Team Rebounds Per Game', 'Assist Pct', 'Assists', 'Assists Per Game', 'Assist to Turnover', 'Steal Pct', 'Steals', 'Steals Per Game', 'Turnover Pct', 'Turnovers', 'Turnovers Per Game', 'Block Pct', 'Blocks', 'Blocks Per Game', 'Fouls', 'Fouls Per Game', 'Disqualifications']

for line in stats_lines:
	array_of_team_stats = line.split(",")
	db_stat = {}
	for i in range(len(mapping)):
		db_stat[mapping[i]] = array_of_team_stats[i]
	team_stat_id =team_stats.insert(db_stat)
