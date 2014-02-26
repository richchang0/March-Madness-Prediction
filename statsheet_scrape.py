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
	url = 'http://statsheet.com/mcb/teams/syracuse/team_stats?type=all'
	soup = get_page(url)
	# print soup
	for table in soup.findAll("table", { "class" : "table-stats" }):
		for tr in table.findAll("tr"):
			tds = tr.findAll("td")
			# print tds
			# this is value
			if len(tds):
				print tds[1].text
	# 	print "-----------------"


def main():
	get_teams()

main()