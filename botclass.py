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


    def setWebhook(self):
        pass


    def deleteWebhook(self):
        pass


    def getWebhookInfo(self):
        pass


    def WebhookInfo(self):
        pass


    def sendMessage(self, chat_id, text):
        param = {
        'chat_id': chat_id,
        'text': text
        }
        self._response = requests.post(self._url
                                       + '/sendMessage', data=param)
        return self._response


    def forwaedMessage(self, chat_id,from_chat_id,
                       message_id, disable_notification=True):
        pass


    def sendPhoto(self, chat_id, photo, **kwargs):
        pass


    def sendAudio(self, chat_id, audio, **kwargs):
        pass


    def sendDocument(self, chat_id, document, **kwargs):
        pass


    def sendVideo(self,chat_id, video, **kwargs):
        pass


    def sendVoice(self, chat_id, voice, **kwargs):
        pass


    def sendVideoNote(self, chat_id, vnote, **kwargs):
        pass


    def sendMediaGroup(self, chat_id, media, **kwargs):
        pass


    def sendLocation(self, latitude, longtitude, **kwargs):
        pass


    def editMessageLiveLocation(self, chat_id, latitude, longtitude, **kwargs):
        pass


    def stopMessageLiveLocation(self, chat_id, **kwargs):
        pass


    def sendVenue(self, chat_id, latitude, longtitude, title, address, **kwargs):
        pass


    def sendCOntact(self, chat_id, phone_num, first_name, **kwargs):
        pass


    def sendChatAction(self, chat_id, action):
        pass


    def getUserProfilePhotos(self, user_id, **kwargs):
        pass


    def kickChatMember(self, chat_id, user_id, until_date=None):
        pass


    def unbanChatMember(self, chat_id, user_id):
        pass


    def restrictChatMember(self, chat_id, user_id, **kwargs):
        pass

    def promoteChatMember(self, chat_id, user_id, **kwargs):
        pass


    def exportChatInviteLink(self, chat_id):
        pass


    def setChatPhoto(self, chat_id, chat_photo):
        pass


    def deleteChatPhoto(self, chat_id):
        pass


    def setChatTitle(self, chat_id, title):
        pass


    def setChatDescription(self, chat_id, message_id,
                           disable_notification=True):
        pass


    def pinChatMessage(self, chat_id, message_id,
                       disable_notification=True):
        pass


    def unpinChatMessage(self, chat_id):
        pass


    def leaveChat(self, chat_id):
        pass


    def getChat(self, chat_id):
        pass


    def getChatAdministrators(self, chat_id):
        pass


    def getChatMembersCount(self, chat_id):
        pass


    def getChatMember(self, chat_id, member_id):
        pass


    def setChatStickerSet(self, chat_id, sticker_set_name):
        pass


    def deleteChatStickerSet(self, chat_id):
        pass


    def answerCallbackQuery(self, callback_query_id, **kwargs):
        pass
