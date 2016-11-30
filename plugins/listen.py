# -*- coding: utf-8 -*-

from slackbot.bot import listen_to

@listen_to('334')
def hansin(message):
    message.send('なんでや！阪神関係ないやろ！')
    message.react('baseball')
