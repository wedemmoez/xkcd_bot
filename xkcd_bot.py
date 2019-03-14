#!/usr/bin/python
import json
import requests
#import token from credentials file
from credentials import *

# URL Helper
def _url(path):
    return 'https://api.ciscospark.com/v1' + path


# Function to get list of all rooms that the bot is a member of
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

# get json information for latest comic
xkcd_json = requests.get("http://xkcd.com/info.0.json").json()
img = xkcd_json[u'img']
# formatted for Spark markown
num = str(xkcd_json[u'num'])
alt = "**Hover Text**: " + xkcd_json[u'alt'] + ' **[permalink](http://xkcd.com/' + num + ')**'

# Get Rooms, Parse JSON, psot to rooms the bot is in
room_dict = get_rooms(token)[u'items']
for i in enumerate(room_dict):
    #post only to rooms labeled as groups, do not send to individuals.
    if room_dict[i][u'type'] == 'group':
        post_file(token, room_dict[i][u'id'], alt, img)
        
