# Functions for buiding the data for our model
import random,os

# Get the stats for the home and away team
def get_stats(home,away):
	fileName = 'stats_2012-2013'
	stats = open("textfiles/stats/" + fileName + ".txt", "r")

	home_stats = []
	away_stats = []

	for line in stats:
		split_line = line.strip("\n").split(",")
		team_name = split_line[0]

		if team_name == home:
			home_stats = split_line
		elif team_name == away:
			away_stats = split_line

	return home_stats, away_stats

# Calculate the delta between the team stats
def calc_delta(home_stats, away_stats, outcome):

	delta_stats = []

	attrLen = len(home_stats)

	for i in range(attrLen):

		val = float(home_stats[i]) - float(away_stats[i])
		delta_stats.append(val)

	if outcome == "NULL":
		rand = random.choice([True, False])
		if rand:
			outcome = 'W'
		else:
			outcome = 'L'


	delta_stats.append(outcome)
	# Append outcome to the result
	# if outcome == 'W':
	# 	delta_stats.append()
	# else:
	# 	delta_stats.append(0)

	return delta_stats


def generate_examples(fileName):

	# fileName = 'march_games'
	outputName = fileName + "_data"
	# outputName = 'march_games_data'

	games = open("textfiles/games/" + fileName + ".txt", "r")
	output = open("textfiles/model_data/" + outputName + ".csv", "w")

	# count = 0
	for match in games:
		# count += 1

		# if count > 2000:
		# 	break
		# else:
		split_line = match.strip("\n").split(",")

		home_team = split_line[0]
		away_team = split_line[1]
		outcome = split_line[2]
		
		home_stats, away_stats = get_stats(home_team, away_team)

		# print home_team + " vs " + away_team
		# print "home length: ", len(home_stats)
		# print "away length: ", len(away_stats)
		# print count

		# if (len(home_stats) == 0) or (len(away_stats) == 0):
		# 	break

		# Remove team name from the list
		home_stats = home_stats[1:]
		away_stats = away_stats[1:]

		
		delta_stats = calc_delta(home_stats,away_stats,outcome)

		delta_str = ",".join(map(str, delta_stats))

		output.write(delta_str + "\n")

	return outputName

# Modify attr_to_delete to remove the attributes that you want 
def remove_attributes(dataFile):
	attr_array = ['Total Games', 'Wins', 'Losses', 'Winning Pct', 'Possessions', 'Possessions Per 40 minutes', 'Floor Pct', 'Efficiency', 'Field Goals Made', 'Field Goal Attempts', 'Field Goal Pct', 'Free Throws Made', 'Free Throw Attempts', 'Free Throw Pct', '3-pt Field Goals Made', '3-pt Field Goal Attempts', '3-pt Field Goal Pct', 'Effective Field Goal Pct', 'True Shooting Pct', 'Free Throw Rate', 'Field Goal Point Pct', 'Free Throw Point Pct', '3-pt Field Goal Point Pct', 'Points Per Possessions', 'Points', 'Points Per Game', 'Rebound Pct', 'Total Rebounds', 'Total Rebounds Per Game', 'Offensive Reb Pct', 'Offensive Rebounds', 'Offensive Rebounds Per Game', 'Defensive Reb Pct', 'Defensive Rebounds', 'Defensive Rebounds Per Game', 'Team Rebounds', 'Team Rebounds Per Game', 'Assist Pct', 'Assists', 'Assists Per Game', 'Assist to Turnover', 'Steal Pct', 'Steals', 'Steals Per Game', 'Turnover Pct', 'Turnovers', 'Turnovers Per Game', 'Block Pct', 'Blocks', 'Blocks Per Game', 'Fouls', 'Fouls Per Game', 'Disqualifications', 'Outcome']

	training_file = open("textfiles/model_data/" + dataFile + ".csv", 'r')
	lines = training_file.readlines()
	new_lines = []

	attr_to_delete = ["Wins", "Losses", "Field Goals Made", "Free Throws Made", "3-pt Field Goals Made"]
	indexes_to_delete = []
	for attr in attr_to_delete:
		indexes_to_delete.append(attr_array.index(attr))

	adjuster = 0
	for index in indexes_to_delete:
		attr_array.pop(index - adjuster)
		adjuster += 1

	header_string = ",".join(attr_array)
	new_lines.append(header_string + "\n")


	for line in lines:
		adjuster = 0
		stat_array = line.split(",")

		for index in indexes_to_delete:
			# print attr_to_delete[i]+":"+stat_array[index]
			stat_array.pop(index - adjuster)
			adjuster += 1
		stat_string = ",".join(stat_array)
		new_lines.append(stat_string)

	training_file2 = open("textfiles/model_data/" + dataFile + "_fixed" + ".csv", "w+")
	training_file2.writelines(new_lines)

	training_file.close()
	os.remove("textfiles/model_data/" + dataFile + ".csv")

def main():

	# gameList = 'games_conf_2012-2013_formatted_unique'
	gameList = 'march_games'

	dataFile = generate_examples(gameList)
	remove_attributes(dataFile)

main()

