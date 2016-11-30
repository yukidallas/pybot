# -*- coding: utf-8 -*-

import json
import urllib.request
from slackbot.bot import respond_to

@respond_to('(.*)')
def talk(message, matchedstr):
    url = 'https://chatbot-api.userlocal.jp/api/chat?'
    params = {
      'message': matchedstr,
      'key': '0efe4d8593840ac3a5c2'
    } 
    params = urllib.parse.urlencode(params)
    url = url + params

    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    message.reply(content['result'])
