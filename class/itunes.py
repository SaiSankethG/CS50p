import json
import requests
import sys
response=requests.get("https://itunes.apple.com/search?entity&limit=50&term=" + sys.argv[1])
o=response.json()
for i in o["results"]:
    print(i["trackName"])
