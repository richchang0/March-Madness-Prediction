import import_db as db

team_array = []
for game in db.game_results.find():

	if db.team_stats.find({ 'Team Name': game['Home']}).count() == 0:
		if game['Home'] not in team_array:
			team_array.append(game['Home'])
			# print game['Home']

output_file = open("unmatchingteams.txt", 'w')
for team in team_array:
	output_file.write(team+"\n")
output_file.close()