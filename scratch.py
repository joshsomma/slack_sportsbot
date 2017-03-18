import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '11b3ad4cfece46049d2cc128c72f6104', 'X-Response-Control': 'minified' }
connection.request('GET', '/v1/competitions', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response)
