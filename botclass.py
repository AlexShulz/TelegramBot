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


    def getUpdates(self, **kwargs):
        """Get new incoming messages from bot"""
        self._offset = kwargs.get('offset', 0)
        self._timeout = kwargs.get('timeout', 0)
        self._limit = kwargs.get('limit', 0)

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


    def setWebhook(self, url, **kwargs):
        data={
        'url': url
        }
        try:
            requests.post(self._url + '/setWebhook', data=data)
            return True
        except:
            return False



    def deleteWebhook(self):
        """Try to delete Webhook. If success returns True, else returns False"""
        try:
            self._request = requests.get(self._url + '/deleteWebhook')
            return True
        except:
            return False

    @property
    def getWebhookInfo(self):
        """Get information about webhook"""
        try:
            self._request = requests.get(self._url + '/getWebhookInfo')
            return self._request
        except:
            return None


    def sendMessage(self, chat_id, text, **kwargs):
        """ Sending a message from bot to specified chat """
        param = {
        'chat_id': chat_id,
        'text': text
        }

        try:
            self._response = requests.post(self._url
                                           + '/sendMessage', data=param)
            return self._response
        except:
            return None


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
