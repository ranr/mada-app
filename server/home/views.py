from django.http import HttpResponse
from django import shortcuts
from django.views.decorators.csrf import csrf_exempt
import json
from models import *
import logging
import os
import distance_earth

logger = logging.getLogger(__name__)

def index(request):
    return shortcuts.render_to_response( 'index.html' )

@csrf_exempt
def nearby_events(request,*args,**kwargs):
    logger.info("Got request body: " + request.body)
    params=json.loads(request.body)
    lat=params["latitude"]
    lon=params["longitude"]

    RADIUS_OF_RELEVANCE_KM=1.2
    logger.info("Got nearby_events request")
    all_events=Event.objects.all()
    events=find_nearby_events(all_events, lat, lon, RADIUS_OF_RELEVANCE_KM)
    response={}    
    events_json=[build_event_json(event) for event in events]
    response["events"]=events_json
    # response["allEvents"]=allEvents
    # logger.info("response: " + str(response))
    response_json=json.dumps(response)
    return HttpResponse(response_json)


def new_event(request, lat, lon):
    logger.info("Got new_events request")
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
