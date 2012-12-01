import urllib
import json
import server

testedServer = server.Server()
rescuer= {
        "name": "Cookie monster",
        "phoneNumber": "666",
        "rank": "trashcan manager",
        "latitude": 32.43243,
        "longitude": 35.432
    }

# No events yet - expect empty response
data = urllib.urlopen( "http://localhost:8000/nearby_events", json.dumps(rescuer) ).read()
result = json.loads( data )
assert (result == {"events":[]})

# Add an event 
data = urllib.urlopen( "http://localhost:8000/new_event/32.43243/35.432").read()
assert (data == "")

# Now expect to get the event back
data = urllib.urlopen( "http://localhost:8000/nearby_events", json.dumps(rescuer) ).read()
result = json.loads( data )
print result
assert (len(result["events"]) == 1)
assert (result["events"][0]["lat"] == rescuer["latitude"])
assert (result["events"][0]["lon"] == rescuer["longitude"])

# Let's have a different rescuer in a different place
rescuer2= {
        "name": "Cookie monster",
        "phoneNumber": "666",
        "rank": "trashcan manager",
        "latitude": 36.43243,
        "longitude": 35.432
    }
data = urllib.urlopen( "http://localhost:8000/nearby_events", json.dumps(rescuer2) ).read()
result = json.loads( data )
assert (result == {"events":[]})

# Open an event more than RADIUS=1.2 kms aways
data = urllib.urlopen( "http://localhost:8000/new_event/36.44343/35.432").read()
assert (data == "")

# Make sure we don't get the event
data = urllib.urlopen( "http://localhost:8000/nearby_events", json.dumps(rescuer2) ).read()
result = json.loads( data )
assert (result == {"events":[]})

# Open an event less than RADIUS=1.2 kms away
data = urllib.urlopen( "http://localhost:8000/new_event/36.44243/35.432").read()
assert (data == "")

# Expect to get the new event
data = urllib.urlopen( "http://localhost:8000/nearby_events", json.dumps(rescuer2) ).read()
result = json.loads( data )
#{'events': [{'lat': 36.44243, 'timestamp': '2012-12-01 14:03:00.571284+00:00', 'lon': 35.432}]}
