attr_array = ['Total Games', 'Wins', 'Losses', 'Winning Pct', 'Possessions', 'Possessions Per 40 minutes', 'Floor Pct', 'Efficiency', 'Field Goals Made', 'Field Goal Attempts', 'Field Goal Pct', 'Free Throws Made', 'Free Throw Attempts', 'Free Throw Pct', '3-pt Field Goals Made', '3-pt Field Goal Attempts', '3-pt Field Goal Pct', 'Effective Field Goal Pct', 'True Shooting Pct', 'Free Throw Rate', 'Field Goal Point Pct', 'Free Throw Point Pct', '3-pt Field Goal Point Pct', 'Points Per Possessions', 'Points', 'Points Per Game', 'Rebound Pct', 'Total Rebounds', 'Total Rebounds Per Game', 'Offensive Reb Pct', 'Offensive Rebounds', 'Offensive Rebounds Per Game', 'Defensive Reb Pct', 'Defensive Rebounds', 'Defensive Rebounds Per Game', 'Team Rebounds', 'Team Rebounds Per Game', 'Assist Pct', 'Assists', 'Assists Per Game', 'Assist to Turnover', 'Steal Pct', 'Steals', 'Steals Per Game', 'Turnover Pct', 'Turnovers', 'Turnovers Per Game', 'Block Pct', 'Blocks', 'Blocks Per Game', 'Fouls', 'Fouls Per Game', 'Disqualifications', 'Outcome']
training_file = open("textfiles/training_data_2012-2013.csv", "rw+")
lines = training_file.readlines()
new_lines = []

attr_to_delete = ["Wins", "Losses", "Field Goals Made", "Free Throws Made", "3-pt Field Goals Made"]
indexes_to_delete = []
for attr in attr_to_delete:
	indexes_to_delete.append(attr_array.index(attr))

for line in lines:
	adjuster = 0
	stat_array = line.split(",")

	for index in indexes_to_delete:
		# print attr_to_delete[i]+":"+stat_array[index]
		# print stat_array.pop(index - adjuster)
		adjuster += 1
	stat_string = ",".join(stat_array)
	new_lines.append(stat_string)
training_file2 = open("textfiles/training_data_fixed.csv", "w+")
training_file2.writelines(new_lines)


