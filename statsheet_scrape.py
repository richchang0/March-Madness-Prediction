from bs4 import BeautifulSoup
from selenium import webdriver
import string

def get_page(url):

	print "getting url: " + url
	driver = webdriver.PhantomJS()
	driver.get(url)
	data = driver.page_source

	driver.quit()
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
					outputFile = open('teams_statsheet.txt', 'a')
					line = str(tds[1].text) + "," + str(tds[1].a['href']) + "," + str(tds[2].text)
					outputFile.write(line + "\n")
					outputFile.close()



def get_stats():

	teamFile = open('teams_statsheet.txt', 'r')
	
	# TargetURL
	# http://statsheet.com/mcb/teams/syracuse/team_stats?season=2013-2014&type=all
	season = '2013-2014'
	extraPart = '/team_stats?season=' + season + '&type=all'

	# url = 'http://statsheet.com/mcb/teams/syracuse/team_stats?type=all'
	for team in teamFile:

		splitLine = team.strip("\n").split(",")
		teamName = splitLine[0]
		teamURL = splitLine[1]

		url = teamURL + extraPart

		soup = get_page(url)
		# print soup
		for table in soup.findAll("table", { "class" : "table-stats" }):

			valueStr = ""
			for tr in table.findAll("tr"):
				tds = tr.findAll("td")

				# this are the values
				if len(tds):
					valueStr += str(tds[1].text) + ","

			if valueStr != "":
				valueStr = valueStr[:-1]
				statFile = open('stats.txt', 'a')
				statFile.write(teamName + "," + valueStr + "\n")
				statFile.close()

	teamFile.close()


def main():
	# get_teams()
	get_stats()

main()