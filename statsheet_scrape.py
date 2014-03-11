from bs4 import BeautifulSoup
from selenium import webdriver
import string, re

# Initialize driver for getting pages
driver = webdriver.PhantomJS()

def get_page(url):

	print "getting url: " + url
	
	# driver = webdriver.PhantomJS()
	driver.get(url)
	data = driver.page_source

	# driver.quit()
	soup = BeautifulSoup(data)

	return soup

def get_teams():
	
	alphabet = list(string.ascii_uppercase)
	baseUrl = "http://statsheet.com/mcb/teams/browse/name?t="

	for letter in alphabet:
		url = baseUrl + letter
		soup = get_page(url)

		for table in soup.findAll("tbody"):
			for tr in table.findAll("tr"):
				tds = tr.findAll("td")
				if len(tds):
					outputFile = open('textfiles/teams_url_names_statsheet.txt', 'a')
					link = str(tds[1].a['href'])
					name_from_link = link.split("/")[-1]
					line =  name_from_link + "," + link + "," + str(tds[2].text)
					outputFile.write(line + "\n")
					outputFile.close()

# IGNORE THIS FUNCTION -- calculating teams in another way..... see clean_data.py
# Doesn't fully work...... not all teams have the Summary section on their pages
def get_home_court():

	teamFile = open('textfiles/teams_url_names_statsheet.txt', 'r')

	for line in teamFile:
		# url = 'http://statsheet.com/mcb/teams/michigan-state'
		splitLine = line.strip("\n").split(",")

		teamURL = splitLine[1]

		soup = get_page(teamURL)
		tableResults = soup.findAll("table")

		detailTable = tableResults[2]
		rows = detailTable.findAll("tr")

		homeCourt = rows[2].findAll("td")[1].a['href'].split("/")[-1]

		print homeCourt

		splitLine.append(homeCourt)

		newLine = ",".join(splitLine)

		newTeamFile = open('textfiles/ff.txt', 'a')
		newTeamFile.write(newLine + "\n")
		newTeamFile.close()

	teamFile.close()

def get_stats():

	# teamFile = open('textfiles/teams_url_names_statsheet.txt', 'r')
	teamFile = open('textfiles/test.txt', 'r')
	
	# TargetURL
	# http://statsheet.com/mcb/teams/syracuse/team_stats?season=2013-2014&type=all
	season = '2011-2012'
	extraPart = '/team_stats?season=' + season + '&type=all'

	# url = "http://statsheet.com/mcb/teams/nebraska-omaha/team_stats?type=all"
	# thearray = [url]
	for team in teamFile:

		splitLine = team.strip("\n").split(",")
		teamName = splitLine[0]
		teamURL = splitLine[1]

		# teamName = "Nebraska-Omaha"
		url = teamURL + extraPart

		soup = get_page(url)
		# print soup

		tableResults = soup.findAll("table", { "class" : "table-stats" })

		if len(tableResults) == 0:
			valueStr = "NULL"
			statFile = open('textfiles/stats_' + season + '.txt', 'a')
			statFile.write(teamName + "," + valueStr + "\n")
			statFile.close()
		else:
			for table in tableResults:

				valueStr = ""
				for tr in table.findAll("tr"):
					tds = tr.findAll("td")

					# this are the values
					if len(tds):
						valueStr += str(tds[1].text) + ","

				if valueStr != "":
					valueStr = valueStr[:-1]
					statFile = open('textfiles/stats_' + season + '.txt', 'a')
					statFile.write(teamName + "," + valueStr + "\n")
					statFile.close()

	teamFile.close()


def get_games():

	# teamFile = open('textfiles/teams_url_names_statsheet.txt', 'r')
	teamFile = open('textfiles/temp_games_list.txt', 'r')

	# Target url
	# http://statsheet.com/mcb/teams/syracuse/schedule?season=2012-2013

	season = '2012-2013'
	extraPart = '/schedule?season=' + season

	for team in teamFile:

		splitLine = team.strip("\n").split(",")
		teamName = splitLine[0]
		teamURL = splitLine[1]

		url = teamURL + extraPart

		soup = get_page(url)

		tableSchedule = soup.findAll("table", { "class" : "sortable" })

		for game in tableSchedule:
			for tr in game.findAll("tr"):
				tds = tr.findAll("td")
				if len(tds):
					opponentTD = tds[5].findAll("a")

					if len(opponentTD) == 1:
						opponentName = opponentTD[0]['href'].split("/")[-1]
					else:
						opponentName = opponentTD[1]['href'].split("/")[-1]

					location = tds[8].a['href'].split("/")[-1]
					isConf = tds[9].text

					# print isConf
					# c = raw_input()

					# only save conference games
					if isConf == "Yes":
						teamScore = tds[2].text
						opponentScore = tds[4].text

						try:
							if int(teamScore) > int(opponentScore):
								outcome = "W"
							else:
								outcome = "L"
						except:
							outcome = "NULL"

						# print "result: " + str(teamScore) + " to " + str(opponentScore) + " at " + location
						resultLine = teamName + "," + opponentName + "," + outcome + "," + location
						print resultLine

						gameFile = open('textfiles/games_conf_' + season + '.txt', 'a')
						gameFile.write(resultLine + "\n")
						gameFile.close()

def main():
	# get_teams()
	# get_home_court()
	# get_stats()
	# get_games()

main()