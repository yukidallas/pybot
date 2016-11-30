# -*- coding: utf-8 -*-

from slackbot.bot import respond_to

@respond_to('こんにちは')
def post(message):
    message.reply('こんにちは！')
