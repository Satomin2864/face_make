from requests_oauthlib import OAuth1Session
import json
import settings
import csv
import urllib.request
# twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
# params = {}
# req = twitter.get("https://api.twitter.com/1.1/followers/ids.json", params = params)

url = 'https://i1.wp.com/xn--zck0ab2mr42rre5d.com/wp-content/uploads/2016/09/fe76bca184c0c08acc548178202595e8.png'
urllib.request.urlretrieve(url, 'mamayu.png')
