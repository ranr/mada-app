import urllib
import json
import server

testedServer = server.Server()
data = urllib.urlopen( "http://localhost:8080/categories" ).read()
result = json.loads( data )
assert result[ 'categories' ] == [ "category1" ]
