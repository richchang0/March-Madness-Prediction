from bs4 import BeautifulSoup

import requests

def get_page(url):

	print "getting url: " + url
	r  = requests.get("http://" +url)
	data = r.text
	soup = BeautifulSoup(data)

	return soup

def scrape_teams():
	url = "espn.go.com/mens-college-basketball/teams"
	soup = get_page(url)
	teamFile = open("teams.txt", 'w')
	
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


def main():
	scrape_teams()


main()