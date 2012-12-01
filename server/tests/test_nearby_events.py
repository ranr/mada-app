import urllib
import json
import server

testedServer = server.Server()
data = urllib.urlopen( "http://localhost:8080/nearby_events/myId/1/2" ).read()
result = json.loads( data )
print result
assert result == [ "category1" ]
