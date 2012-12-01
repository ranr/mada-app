import urllib
import json
import server

testedServer = server.Server()
rescuer= {
        "name": "Cookie monster",
        "phone_number": "052-555-4444",
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

# Check that rescuer exists now
returned_rescuer=server.get_rescuer_by_phone(rescuer["phone_number"])
assert(returned_rescuer)
assert(returned_rescuer["phone_number"]==rescuer["phone_number"])
common_keys=[key for key in rescuer.keys() if key in returned_rescuer.keys()]
expected_keys=sorted(['phone_number', 'latitude', 'longitude', 'rank'])

assert(expected_keys==sorted(common_keys) )
for key in common_keys:
    assert(returned_rescuer[key]==rescuer[key]) 

# Now expect to get the event back
data = urllib.urlopen( "http://localhost:8000/nearby_events", json.dumps(rescuer) ).read()
result = json.loads( data )
print result
assert (len(result["events"]) == 1)
assert (result["events"][0]["latitude"] == rescuer["latitude"])
assert (result["events"][0]["longitude"] == rescuer["longitude"])

# Let's have a different rescuer in a different place
rescuer2= {
        "name": "Cookie monster",
        "phone_number": "052-666-3333",
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
assert (len(result["events"]) == 1)
assert (result["events"][0]["latitude"] == 36.44243)
assert (result["events"][0]["longitude"] == 35.432)


