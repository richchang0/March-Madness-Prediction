# Functions for buiding the data for our model

# Get the stats for the home and away team
def get_stats(home,away):
	fileName = 'stats_2012-2013'
	stats = open("textfiles/" + fileName + ".txt", "r")

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


	delta_stats.append(outcome)
	# Append outcome to the result
	# if outcome == 'W':
	# 	delta_stats.append()
	# else:
	# 	delta_stats.append(0)

	return delta_stats


def generate_examples():

	fileName = 'games_conf_2012-2013_formatted_unique'
	outputName = 'training_data_2012-2013'

	games = open("textfiles/" + fileName + ".txt", "r")
	output = open("textfiles/" + outputName + ".txt", "w")

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

def main():
	generate_examples()


main()

