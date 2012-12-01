from django.http import HttpResponse
from django import shortcuts
import json

def index(request):
    return shortcuts.render_to_response( 'index.html' )

def categories(request):
    return json.dumps(['categories_2'])
