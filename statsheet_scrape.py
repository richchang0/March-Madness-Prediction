from bs4 import BeautifulSoup
from selenium import webdriver

def get_page(url):

	print "getting url: " + url
	driver = webdriver.PhantomJS()
	driver.get(url)
	data = driver.page_source

	driver.quit()
	soup = BeautifulSoup(data)

	return soup

def get_teams():
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