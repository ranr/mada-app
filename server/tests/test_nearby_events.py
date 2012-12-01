import urllib
import json
import server

testedServer = server.Server()
event= {
        "name": "Cookie monster",
        "phoneNumber": "666",
        "rank": "trashcan manager",
        "latitude": 32.43243,
        "longitude": 35.432
    }
data = urllib.urlopen( "http://localhost:8000/nearby_events", json.dumps(event) ).read()
result = json.loads( data )
assert (result == {"events":[]})
