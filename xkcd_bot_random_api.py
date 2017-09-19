#!/usr/bin/python
# this sparkbot is just for testing. will post only to the GDT sparkbot testing room. 
import json
import random as r
import requests
from credentials import *
from ciscosparkapi import CiscoSparkAPI

#Create API call - 😛 🤑
api = CiscoSparkAPI(access_token=api_token)

xkcd_json = requests.get("http://xkcd.com/info.0.json").json()
# formatted for Spark markown 💩
num = str(r.randrange(0, xkcd_json[u'num'], 1))
xkcd_json = requests.get("http://xkcd.com/"+num+"/info.0.json").json()
xkcd_json[u'alt'] = "**Hover Text**: " + xkcd_json[u'alt'] + ' **[permalink](http://xkcd.com/' + num + ')**'
# API wrapper expects a list of files. We made it a list. 🖕
img= [xkcd_json[u'img']]
# Get Rooms, Parse JSON, psot to rooms the bot is in 🗣 👤 👥 
rooms = api.rooms.list(type='group')
for room in rooms:
    api.messages.create(roomId=room.id,markdown=xkcd_json[u'alt'], files=img)