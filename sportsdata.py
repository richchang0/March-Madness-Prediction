import urllib2
import xml.etree.ElementTree as xml

apikey = "xzj9acn7kgjpv3syngfbu7h4"
access_level = "t"
version = "3"

def schedule(year, season):
	url =  "http://api.sportsdatallc.org/ncaamb-"+access_level+version+"/games/"+year+"/"+season+"/schedule.xml?api_key="+apikey
	clean = "{http://feed.elasticstats.com/schema/basketball/schedule-v2.0.xsd}"
	response = urllib2.urlopen(url)
	games(response, clean)

def games(response, clean=""):
	games = {}
	hometeam = ""
	awayteam = ""
	tree = xml.parse(response)
	root = tree.getroot()
	for elem in root.iter():
		tag = elem.tag.replace(clean,"")

		if tag == "home":
			hometeam = elem.attrib["name"]
		elif tag == "away":
			awayteam = elem.attrib["name"]
		elif tag == "game":
			games[hometeam+" vs "+awayteam] =  elem.attrib["id"]
	pretty_print_games(games)
	return games

def pretty_print_games(games):
	for game in games.keys():
		print game
		print games[game] + "\n"


def main():
	schedule("2013", "reg")


main()