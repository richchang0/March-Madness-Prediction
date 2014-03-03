import import_db as db

team_array = []
for game in db.game_results.find():

	if db.team_stats.find({ 'Team Name': game['Home']}).count() == 0:
		if game['Home'] not in team_array:
			team_array.append(game['Home'])
			print game['Home']
