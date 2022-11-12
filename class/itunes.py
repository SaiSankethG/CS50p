import requests
import sys
response=requests.get("https://itunes.apple.com/search?entity&limit=1&term=" + sys.argv[1])
print(response)