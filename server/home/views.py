from django.http import HttpResponse
from django import shortcuts
import json
from models import *
import logging
import os
import distance_earth

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
    return [event for event in events if distance_earth.distance_on_earth(event.lat, event.lon, lat, lon) < radius]
