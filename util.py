import import_db as db

def get_missing_team_names():
	team_array = []
	for game in db.game_results.find():

		if db.team_stats.find({ 'Team Name': game['Away']}).count() == 0:
			if game['Away'] not in team_array:
				team_array.append(game['Away'])
				# print game['Home']

	output_file = open("textfiles/unmatchingteams.txt", 'w')
	for team in team_array:
		output_file.write(team+"\n")
	output_file.close()

def find_manual_match(espn_name):

	# manually_matched_file = open("textfiles/richs_list.txt", 'r')
	manually_matched_file = open("textfiles/allens_list.txt", 'r')

	for line in manually_matched_file:
		splitLine = line.strip("\n").split(",")
		if espn_name == splitLine[0]:
			# If matches, return our match
			stat_sheet_name = splitLine[1]
			if stat_sheet_name != "?":
				return splitLine[1]

	manually_matched_file.close()
	return 0

def match_names():

	unmatched_team_file = open("textfiles/unmatchingteams.txt", 'r')
	# unmatched_team_file = open("still_unmatched.txt", 'r')

	matched_file = open('new_matched.txt', 'w')
	still_unmatched_file = open('new_still_unmatched.txt', 'w')

	for unmatchedLine in unmatched_team_file:
		splitLine = unmatchedLine.strip("\n").split(",")

		espn_name = splitLine[0]
		matched_name = find_manual_match(espn_name)

		if matched_name != 0:
			matched_file.write(espn_name + "," + matched_name + "\n")
		else:
			still_unmatched_file.write(espn_name + "\n")


	unmatched_team_file.close()
	matched_file.close()
	still_unmatched_file.close()


def find_match(stat_name):
	matched_names = open("textfiles/matched.txt", "r")

	for line in matched_names:
		splitLine = line.strip("\n").split(",")
		fileStatName = splitLine[1]
		if stat_name == fileStatName:
			espn_name = splitLine[0]
			return espn_name

	return 0


def replace_statsheet_names():
	stat_file = open("textfiles/stats.txt", "r")

	modified_stat_file = open("modified_stats.txt", "w")

	for line in stat_file:
		splitLine = line.strip("\n").split(",")
		statName = splitLine[0]

		espn_name = find_match(statName)
		if espn_name != 0:
			splitLine[0] = espn_name

		line = ",".join(map(str, splitLine))

		modified_stat_file.write(line + "\n")
	
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]


def determine_home_court():
	gameFile = open('textfiles/games_2012-2013.txt', 'r')

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
				teamHomeFile = open('textfiles/team_home_matches.txt', 'a')
				teamHomeFile.write(prevTeamName + "," + homeCourt + "\n")
				teamHomeFile.close()
			prevTeamName = curTeamName
			locations = {}

		# Build dictionary for getting the counts
		if curLocation in locations:
			locations[curLocation] += 1
		else:
			locations[curLocation] = 1

def write_team_with_home():

	homeFile = open('textfiles/team_home_matches.txt', 'r')
	teamFile = open('textfiles/teams_url_names_statsheet.txt', 'r')

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

		newTeamFile = open('textfiles/team_with_home_statsheet.txt', 'a')
		newTeamFile.write(newLine + "\n")
		newTeamFile.close()


def main():
	# get_missing_team_names()
	# match_names()
	# replace_statsheet_names()
	# determine_home_court()
	# write_team_with_home()

main()
