from django.http import HttpResponse
from django import shortcuts
from django.views.decorators.csrf import csrf_exempt
import json
from models import *
import logging
import os
import distance_earth
from django.core import serializers
import datetime

RADIUS_OF_RELEVANCE_KM=1.2
logger = logging.getLogger(__name__)

def index(request):
    return shortcuts.render_to_response( 'index.html' )

@csrf_exempt
def nearby_events(request,*args,**kwargs):
    logger.info("Got request body: " + request.body)
    params=json.loads(request.body)
    lat=params["latitude"]
    lon=params["longitude"]

    logger.info("Got nearby_events request")
    latestEvents=Event.objects.filter( timestamp__gt = datetime.datetime.now() - datetime.timedelta( minutes = 20 ) )
    events=find_nearby_events(latestEvents, lat, lon, RADIUS_OF_RELEVANCE_KM)
    response_json=generate_events_response(events)
    update_rescuer(params)
    return HttpResponse(response_json)

@csrf_exempt
def new_event(request, lat, lon):
    logger.info("Got new_events request. lat=%s long=%s" % (lat,lon))
    lat=float(lat)
    lon=float(lon)
    event = Event(latitude=lat, longitude=lon)
    event.save()
    return HttpResponse(json.dumps(build_event_dict(event)))

@csrf_exempt
def all_events(request):
    logger.info("Got all_events request")
    all_events=Event.objects.all()
    response_json=generate_events_response(all_events)
    return HttpResponse(response_json)

@csrf_exempt
def remove_event(request, id):
    logger.info("Got delete request id=%s" % id)
    events=Event.objects.filter(id=id)
    events.delete()
    return HttpResponse(json.dumps({}))

@csrf_exempt
def get_rescuer(request, phone_number):
    logger.info("get_rescuer called! phone number: " + phone_number)
    rescuers=get_rescuers_by_phone(phone_number)
    logger.info("rescuers: " + str(rescuers))
    if (rescuers != []):
        d=build_rescuer_dict(rescuers[0])
        return HttpResponse(json.dumps(d))
    else: 
        return HttpResponse(json.dumps({}))

@csrf_exempt
def all_rescuers(request):
    logger.info("all_rescuers called!")
    rescuers=Rescuer.objects.all()
    data = serializers.serialize('json', rescuers)
    return HttpResponse(json.dumps([x["fields"] for x in json.loads(data)]))

def update_rescuer(params):
    rescuers=get_rescuers_by_phone(params["phone_number"])
    
    logger.info("%s %s" % (type(rescuers), rescuers))
    if (rescuers == []):
        rescuer = Rescuer(latitude=params["latitude"], longitude=params["longitude"],
            rank=params["rank"], phone_number=params["phone_number"])
        logger.info("New rescuer!")
    else:
        rescuer = rescuers[0]  # This is a unique field. There will always be just one
        logger.info("I know this rescuer!")
    rescuer.save()
    logger.info("Saved rescuer")
       

def get_rescuers_by_phone(phone_number):
    rescuers=list(Rescuer.objects.filter(phone_number=phone_number))
    return rescuers

def generate_events_response(events):
    response={}    
    events_dict=[build_event_dict(event) for event in events]
    response["events"]=events_dict
    # response["allEvents"]=allEvents
    # logger.info("response: " + str(response))
    response_json=json.dumps(response)
    return response_json

def build_event_dict(event):
    event.information = "HEART ATTACK"
    event.address     = "Diezengoff 99"
    data = serializers.serialize('json', [event])
    result=json.loads(data)[0]['fields']
    result["id"]=event.id
    return result

    
def build_rescuer_dict(rescuer):
    data = serializers.serialize('json', [rescuer])
    return json.loads(data)[0]['fields']

def find_nearby_events(events, lat, lon, radius):
    return [event for event in events if distance_earth.distance_on_earth(event.latitude, event.longitude, lat, lon) < radius]
