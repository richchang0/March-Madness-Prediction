import import_db as db

def get_missing_team_names():
	team_array = []
	for game in db.game_results.find():

		if db.team_stats.find({ 'Team Name': game['Home']}).count() == 0:
			if game['Home'] not in team_array:
				team_array.append(game['Home'])
				# print game['Home']

	output_file = open("textfiles/unmatchingteams.txt", 'w')
	for team in team_array:
		output_file.write(team+"\n")
	output_file.close()

def match_names():

	unmatched_team_file = open("textfiles/unmatchingteams.txt", 'r')
	# manually_matched_file = open("richs_list.txt", 'r')

	# matched_file = open('matched.txt', 'w')
	# still_unmatched_file = open('matched.txt', 'w')

	for unmatchedLine in unmatched_team_file:
		splitLine = unmatchedLine.strip("\n").split("")
		print splitLine[0]


def main():
	# get_missing_team_names()
	match_names()

