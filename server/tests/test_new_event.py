import urllib
import json
import server


testedServer = server.Server()
id=server.create_event(5,7)
print "id=%s" % id
