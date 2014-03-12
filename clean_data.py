# Script for figuring out home court for teams and formatting the input from statsheet 
# into a format that works with our build_examples.py that generates data for the model

def determine_home_court():
	gameFile = open('textfiles/games/games_2012-2013.txt', 'r')

	prevTeamName = ""

	locations = {}

	for line in gameFile:
		splitLine = line.strip("\n").split(",")

		curTeamName = splitLine[0]
		curLocation = splitLine[3]

		# print curTeamName
		if curTeamName != prevTeamName:
			# Skips the first instance
			if prevTeamName != "":
				homeCourt = keywithmaxval(locations)
				print prevTeamName + "," + homeCourt
				teamHomeFile = open('textfiles/teams/team_home_matches.txt', 'a')
				teamHomeFile.write(prevTeamName + "," + homeCourt + "\n")
				teamHomeFile.close()
			prevTeamName = curTeamName
			locations = {}

		# Build dictionary for getting the counts
		if curLocation in locations:
			locations[curLocation] += 1
		else:
			locations[curLocation] = 1

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def write_team_with_home():

	homeFile = open('textfiles/teams/team_home_matches.txt', 'r')
	teamFile = open('textfiles/teams/teams_url_names_statsheet.txt', 'r')

	teamHomeMappings = {}

	# build the team --> homecourt dictionary
	for line in homeFile:
		splitLine = line.strip("\n").split(",")
		teamName = splitLine[0]
		homeCourt = splitLine[1]

		if teamName not in teamHomeMappings:
			teamHomeMappings[teamName] = homeCourt

	for team in teamFile:
		splitLine = team.strip("\n").split(",")
		teamName = splitLine[0]

		# Default value for home if not found in dictionary
		home = "NULL"

		if teamName in teamHomeMappings:
			home = teamHomeMappings[teamName]

		splitLine.append(home)

		newLine = ",".join(splitLine)

		newTeamFile = open('textfiles/teams/team_with_home_statsheet.txt', 'a')
		newTeamFile.write(newLine + "\n")
		newTeamFile.close()

# Search for team that matches name and returns the home team
def get_home_court(name):
	# print "looking for hometeam for: " + name
	teamFile = open('textfiles/teams/teams_url_names_statsheet.txt', 'r')

	for team in teamFile:
		splitLine = team.strip("\n").split(",")
		teamName = splitLine[0]
		homeCourt = splitLine[3]

		if name == teamName:
			# Note that there are going to be some teams with NULL as their home court
			return homeCourt

	# If not returned by now, that means, the team is not there for some reason?.....
	return "NULL"

# Iterate through game file and rewrite in the following format
#	homeTeam,awayTeam,outcomeForHomeTeam
def adjust_game_format():

	fileName = 'games_conf_2012-2013'
	# fileName = 'test'

	gameFile = open('textfiles/games/' + fileName + '.txt', 'r')

	for game in gameFile:
		splitLine = game.strip("\n").split(",")
		firstTeam = splitLine[0]
		secondTeam = splitLine[1]
		outcome = splitLine[2]
		location = splitLine[3]

		homeCourt = get_home_court(firstTeam)

		# only write if homeCourt is not NULL, null will only occur if the team isn't a D1 team
		if homeCourt != "NULL":
			if location == homeCourt:
				updatedFormat = firstTeam + "," + secondTeam + "," + outcome
			else:
				adjustedOutcome = ""
				if outcome == "W":
					adjustedOutcome = "L"
				else:
					adjustedOutcome = "W"

				updatedFormat = secondTeam + "," + firstTeam + "," + adjustedOutcome

			fixedGameFile = open('textfiles/games/' + fileName + "_formatted"  + ".txt", 'a')
			fixedGameFile.write(updatedFormat + "\n")
			fixedGameFile.close()

# Remove duplicate games that are produced as a result of the way that games are scraped and 
# 	processed from statsheet/our scripts
def remove_duplicate_games():
	# print "in remove_duplicate_games"
	fileName = 'games_conf_2012-2013_formatted'
	gameFile = open("textfiles/games/" + fileName + ".txt", 'r')

	seenGames = []
	for game in gameFile:
		cleanGame = game.strip("\n")

		if cleanGame not in seenGames:
			seenGames.append(cleanGame)

	# Write unique games to file
	uniqueGameFile = open("textfiles/games/" + fileName + "_unique.txt", 'w')
	for uniqGame in seenGames:
		uniqueGameFile.write(uniqGame + "\n")

	uniqueGameFile.close()


def main():
	# determine_home_court()
	# write_team_with_home()
	# adjust_game_format()
	# remove_duplicate_games()

main()