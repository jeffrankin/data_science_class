import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
# for tweet in response[results]:
#     print tweet[text]

print json.load(response)