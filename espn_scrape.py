from bs4 import BeautifulSoup

import requests

def get_page(url):

	print "getting url: " + url
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)

	return soup

# Scrape ESPN NCAAB Site to gather a list of Teams and their Associated Conferences
def get_teams():
	url = "http://espn.go.com/mens-college-basketball/teams"
	soup = get_page(url)
	teamFile = open("textfiles/temp.txt", 'w')
	
	for conf_div in soup.findAll("div", { "class" : "mod-teams-list-medium" }):
		
		conference = conf_div.div.text
		print conf_div.div.text

		teamFile.write(conference + "\n")

		for team_list in conf_div.findAll("div", {"class": "mod-content"}):
			for team in team_list.findAll("a", {"class": "bi"}):
				teamFile.write(str(team.string) + "," + str(team['href']) + "\n")
				print team.string, team['href']

		teamFile.write("-\n")
		print "-----------------"

	teamFile.close()


def get_players():

	teamFile = open("textfiles/teams.txt", 'r')

	confGroup = ""
	for line in teamFile:
		splitLine = line.strip("\n").split(",")

		if len(splitLine) == 1:
			# ignore end of conference indicator
			if splitLine[0] != "-":
				print splitLine[0]
				confGroup = splitLine[0]
		else:

			teamName = splitLine[0]
			rosterUrl = modify_url(splitLine[1], 'roster')

			soup = get_page(rosterUrl)
			for playerRow in soup.findAll("tr"):
				# print playerRow
				playerStr = ""
				for playerData in playerRow.findAll("td"):
					playerStr += str(playerData.text) + ","

				# Strip trailing ","
				playerStr = playerStr[:-1]

				playerFile = open("textfiles/players2.txt", 'a')
				playerFile.write(teamName + "," + confGroup + "," + playerStr + "\n")
				playerFile.close()

	teamFile.close()

def get_games():
	team_file = open('textfiles/teams.txt', 'r')
	lines = team_file.readlines()

	for line in lines:
		line_array = line.split(",")
		if len(line_array) < 2:
			continue
		team_name = line_array[0]
		url = line_array[1]
		soup = get_page(url)
		gameFile = open('textfiles/games.txt', 'a')
		for tr in soup.findAll("tr"):
			ret_line = ""
			if tr["class"][0] not in ['stathead', 'colhead']:
				game_status = tr.findAll("li", {"class":"game-status"})
				opponent_team_name= tr.findAll("li", {"class":"team-name"})[0].text

				opponent_team_name = opponent_team_name.replace("*","") 
				opponent_team_name = re.sub(r'^#\d{1,2}[\W_]? ',"", opponent_team_name)
				# opponent_team_name = re.sub(r'\([^\(]*\)',"", opponent_team_name)
				if len(game_status)>1:

					if game_status[0].text == "@":
						ret_line+=opponent_team_name+","
						ret_line+=team_name+","
						if game_status[1].span.text == "W":
							ret_line+= "L"
						else:
							ret_line+= "W"
					else:
						ret_line+=team_name+","
						ret_line+=opponent_team_name+","

						if game_status[1].span.text == "W":
							ret_line+= "W"
						else:
							ret_line+= "L"
			ret_line+="\n"
			if ret_line != "\n":
				gameFile.write(ret_line)
	gameFile.close()	

# Modify ESPN Url to get either "roster" or "stats"
def modify_url(url, target):
	splitURL = url.split("_")
	newURL = splitURL[0] + target + "/_" + splitURL[1] 
	return newURL

def main():
	get_teams()
	# get_players()


main()