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

def boxscore(game_id):
	url = "http://api.sportsdatallc.org/ncaamb-"+access_level+version
	url += "/games/"+game_id+"/boxscore.xml?api_key=" + apikey
	clean = "{http://feed.elasticstats.com/schema/basketball/game-v2.0.xsd}"
	response = urllib2.urlopen(url)
	xmlprint(response, clean)

def games(response, clean=""):
	games = {}
	hometeam = ""
	awayteam = ""
	tree = xml.parse(response)
	root = tree.getroot()
	for elem in root.iter():
		tag = elem.tag.replace(clean,"")
		# print tag, elem.attrib

		if tag == "home":
			hometeam = elem.attrib["name"]
		elif tag == "away":
			awayteam = elem.attrib["name"]
		elif tag == "game":
			games[hometeam+" vs "+awayteam] =  elem.attrib["id"]
	pretty_print_games(games)
	return games

def xmlprint(response, clean=""):
	tree = xml.parse(response)
	root = tree.getroot()
	for elem in root.iter():
		tag = elem.tag.replace(clean,"")
		print tag, elem.attrib

def pretty_print_games(games):
	i = 1
	for game in games.keys():
		print str(i)+" " +game
		print games[game] + "\n"
		i = i+1


def main():
	schedule("2013", "reg")
	boxscore("19002441-f389-46e4-bdd3-dbe643111a8c")#Charleston Cougars vs Miami (FL) Hurricanes


main()