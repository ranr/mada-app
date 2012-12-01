from django.http import HttpResponse
from django import shortcuts
import json
from models import *
import logging
import os

def index(request):
    return shortcuts.render_to_response( 'index.html' )

def nearby_events(request, id, lat, lon):
    RADIUS_OF_RELEVANCE_KM=1.2
    logging.info("Got nearby_events request")
    all_events=Event.objects.all()
    events=find_nearby_events(all_events, lat, lon, RADIUS_OF_RELEVANCE_KM)
    response={}    
    events_json=[build_event_json(event) for event in events]
    response["events"]=events_json
    # response["allEvents"]=allEvents
    # logging.info("response: " + str(response))
    response_json=json.dumps(response)
    return HttpResponse(response_json)


def new_event(request, lat, lon):
    logging.info("Got new_events request")
    event = Event(lat=lat, lon=lon)
    event.save()
    return HttpResponse("")

def build_event_json(event):
    return {
        'timestamp': str(event.timestamp),
        'lat': str(event.lat),
        'lon': str(event.lon)
    }


def find_nearby_events(events, lat, lon, radius):
    return [event for event in events if distance_on_earth(event.lat, event.lon, lat, lon) < radius]

def distance_on_earth(lat1, long1, lat2, long2):
    import math
    RADIUS_OF_EARTH_KM=6378
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    return arc * RADIUS_OF_EARTH_KM
