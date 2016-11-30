# -*- coding: utf-8 -*-

import json
import urllib.request
from slackbot.bot import respond_to

@respond_to('天気')
def check_weather(message):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    code = '130010'
    
    html = urllib.request.urlopen(url+code)
    jsonfile = json.loads(html.read().decode('utf-8'))
    text = jsonfile['description']['text']

    message.send(text)
