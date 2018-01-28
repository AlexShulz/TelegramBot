#!/usb/bin/python3
# -*- coding: utf-8 -*-
import requests


class TelBotClass(object):
    def __init__(self, token):
        self._token = token
        self._url = "https://api.telegram.org/bot"
        self._offset = 0
        self._timeout = 0
        self._limit = 0


    def getUpdates(self, **kwargs):
        if "offset" in kwargs.keys():
            self._offset = kwargs['offset']
        if "timeout" in kwargs.keys():
            self._timeout = kwargs['timeout']
        if "limit" in kwargs.keys():
            self._limit = kwargs['limit']
        data = {
        'offset': self._offset,
        'limit': self._limit,
        'timeout': self._timeout
        }
        try:
            self._request = requests.post(self._url + self._token + "/getUpdates", data=data)
            if self._request.status_code != 200 or not self._request.json()['ok']:
                return None
            else:
                return self._request.json()['result']

        except:
            return None
