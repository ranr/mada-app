import urllib
import json
import server

testedServer = server.Server()
data = urllib.urlopen( "http://localhost:8000/new_event/32.43243/35.432").read()
assert (result == {"events":[]})
