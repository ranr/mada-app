import urllib
import json
import server


testedServer = server.Server()
data = urllib.urlopen( "http://localhost:8000/all_events").read()
result = json.loads( data )
assert (result["events"] == [])

server.create_event(5,5)

result=server.all_events()
print result
assert (len(result["events"]) == 1)
assert (result["events"][0]["latitude"] == 5)
assert (result["events"][0]["longitude"] == 5)


