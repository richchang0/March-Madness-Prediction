import urllib2

access_level = "t"
version = "3"
api_key = "xzj9acn7kgjpv3syngfbu7h4"

def do_something():
	url = "http://api.sportsdatallc.org/ncaamb-t3/schema/team-v2.0.xsd?api_key=xzj9acn7kgjpv3syngfbu7h4"
	content = urllib2.urlopen(url).read()
	print content

do_something()
