import json
import requests
from credentials import *
from ciscosparkapi import CiscoSparkAPI

#Create API call - 😛 🤑
api = CiscoSparkAPI(access_token=api_token)

xkcd_json = requests.get("http://xkcd.com/info.0.json").json()
# API wrapper expects a list of files. We made it a list. 🖕
img= [xkcd_json[u'img']]
# formatted for Spark markown 💩
num = str(xkcd_json[u'num'])
xkcd_json[u'alt'] = "**Hover Text**: " + xkcd_json[u'alt'] + ' **[permalink](http://xkcd.com/' + num + ')**'
# Get Rooms, Parse JSON, psot to rooms the bot is in 🗣 👤 👥 
rooms = api.rooms.list(type='group')
for room in rooms:
    api.messages.create(roomId=room.id,markdown=xkcd_json[u'alt'], files=img)