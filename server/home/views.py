from django.http import HttpResponse
from django import shortcuts
import json
from models import *
import logging
import os

def index(request):
    return shortcuts.render_to_response( 'index.html' )

def nearby_events(request, id, lat, long):
    logging.info(os.environ)
    logging.info("Got nearby_events request")
    allEvents=Event.objects.all()
    response={}
    # response["allEvents"]=allEvents
    # logging.info("response: " + str(response))
    response_json=json.dumps(response)
    return HttpResponse(response_json)
