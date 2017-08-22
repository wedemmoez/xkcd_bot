#!/usr/bin/python

import json
import random as r
import requests

# URL Helper
def _url(path):
    return 'https://api.ciscospark.com/v1' + path


# Function to get list of rooms
def get_rooms(at):
    headers = {'Authorization': at, 'content-type': 'application/json; charset=utf-8'}
    resp = requests.get(url=_url('/rooms'), headers = headers)
    file_dict = json.loads(resp.text)
    return file_dict

# Function to post file
def post_file(at, roomId, markdown, url=''):
    headers = {'Authorization': at, 'content-type': 'application/json; charset=utf-8'}
    payload = {'roomId': roomId, 'markdown': markdown}
    if url:
        payload['files'] = url
    resp = requests.post(url=_url('/messages'), json=payload, headers=headers)
    file_dict = json.loads(resp.text)
    file_dict['statuscode'] = str(resp.status_code)
    return file_dict

#important stuff
token = "Bearer NjJkM2NkZTEtOTY4NS00N2UyLWIzMTEtZDFmYzA5M2JjNmYwZmVlYmY0OTgtZWI5"

xkcd_json = requests.get("http://xkcd.com/info.0.json").json()
num = str(r.randrange(0, xkcd_json[u'num'], 1))
# pull json for random comic
xkcd_json = requests.get("http://xkcd.com/"+num+"/info.0.json").json()
img = xkcd_json[u'img']
# formatted for Spark markown
alt = "**Caption**: " + xkcd_json[u'alt'] + ' **[permalink](http://xkcd.com/' + num + ')**'

# Get Rooms, Parse JSON, psot to rooms tha bot is in
room_dict = get_rooms(token)[u'items']
for i in range(0, len(room_dict)):
    if room_dict[i][u'type'] == 'group':
        post_file(token, room_dict[i][u'id'], alt, img)
