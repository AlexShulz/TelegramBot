#!/usb/bin/python3
# -*- coding: utf-8 -*-
"""TelegramBot
version = 0.1
author Alexey Preyzner
"""
import requests


class TelBotClass(object):
    def __init__(self, token):
        self._token = token
        self._url = "https://api.telegram.org/bot" + self._token
        self._offset = 0
        self._timeout = 0
        self._limit = 0


    def getUpdates(self, **kwargs):
        if 'offset' in kwargs.keys():
            self._offset = kwargs['offset']
        if 'timeout' in kwargs.keys():
            self._timeout = kwargs['timeout']
        if 'limit' in kwargs.keys():
            self._limit = kwargs['limit']
        data = {
        'offset': self._offset,
        'limit': self._limit,
        'timeout': self._timeout
        }
        try:
            self._request = requests.post(self._url + '/getUpdates', data=data)
            if (self._request.status_code != 200
                or not self._request.json()['ok']):
                return None
            else:
                return self._request.json()['result']

        except:
            return None


    def getUpdate(self, data):
        pass


    def getChat(self, update):
        pass


    def sendMessage(self, chat_id, text):
        param = {
        'chat_id': chat_id,
        'text': text
        }
        self._response = requests.post(self._url
                                       + '/sendMessage', data=param)
        return self._response


    def setWebhook(self):
        pass


    def deleteWebhook(self):
        pass


    def getWebhookInfo(self):
        pass


    def WebhookInfo(self):
        pass
