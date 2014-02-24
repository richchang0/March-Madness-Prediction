import urllib2
import xml.etree.ElementTree as xml

apikey = "xzj9acn7kgjpv3syngfbu7h4"
access_level = "t"
version = "3"

def schedule(year, season):
	url =  "http://api.sportsdatallc.org/ncaamb-"+access_level+version+"/games/"+year+"/"+season+"/schedule.xml?api_key="+apikey
	clean = "{http://feed.elasticstats.com/schema/basketball/schedule-v2.0.xsd}"
	response = urllib2.urlopen(url)
	xmlprint(response, clean)

def xmlprint(response, clean=""):
	tree = xml.parse(response)
	root = tree.getroot()
	for elem in root.iter():
		print elem.tag.replace(clean,""), elem.attrib

def main():
	schedule("2013", "reg")

main()