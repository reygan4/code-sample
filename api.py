import urllib2
import json
locu_api = '5906b0ec1daf64116755d36eeaa9a4239bd9f097'

url = 'https://api.locu.com/v1_0/venue/search/?has_menu=true&api_key=5906b0ec1daf64116755d36eeaa9a4239bd9f097'
obj = json.load(urllib2.urlopen(url))

for i in obj['objects']:
    print i['locality']
