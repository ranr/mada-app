import subprocess
import atexit
import time
import urllib
import json

class Server:
    def __init__( self ):
        self._process = subprocess.Popen( [ "/usr/bin/python", "manage.py",
                            "testserver" ], close_fds = True, shell = False )
        atexit.register( self._destroy )
        time.sleep( 2 )

    def _destroy( self, * args, ** kwargs ):
        self._process.terminate()



def create_event(lat, lon):
    data = urllib.urlopen( "http://localhost:8000/new_event/%f/%f" % (lat, lon)).read()
    assert (data == "")

def all_events():
    data = urllib.urlopen( "http://localhost:8000/all_events").read()
    result = json.loads( data )
    return result

