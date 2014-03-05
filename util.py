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
	

def main():
	# get_missing_team_names()
	# match_names()
	# replace_statsheet_names()

main()
