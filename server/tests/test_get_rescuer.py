import urllib
import json
import server


testedServer = server.Server()
data = urllib.urlopen( "http://localhost:8000/get_rescuer/053-2342432").read()
print data
assert (data == "")
