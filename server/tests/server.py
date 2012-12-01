import subprocess
import atexit
import time

class Server:
    def __init__( self ):
        self._process = subprocess.Popen( [ "/usr/bin/python", "/usr/local/bin/dev_appserver.py",
                            "server", "--use_sqlite" ] )
        atexit.register( self._destroy )
        time.sleep( 2 )

    def _destroy( self, * args, ** kwargs ):
        self._process.terminate()