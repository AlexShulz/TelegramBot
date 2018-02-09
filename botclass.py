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

        self._response = requests.post(self._url
                                       + '/sendMessage', data=param)
        return self._response


    def forwardMessage(self, chat_id,from_chat_id,
                       message_id, disable_notification=True):
        data = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'disable_notification': disable_notification
        }
        try:
            self._response = requests.post(self._url + '/forwardMessage',
                                           data=data)
        except:
            return None
        else:
            return self._response


    def sendPhoto(self, chat_id, photo, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files = {
        'photo': open(photo, 'rb')
        }
        try:
            self._response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return self._response


    def sendAudio(self, chat_id, audio, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'duration': kwargs.get('duration', None),
        'performer': kwargs.get('performer', None),
        'title': kwargs.get('title', None),
        'disable_notification': kwargs.get('disable_notification', False)
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files = {
        'audio': open(audio, 'rb')
        }
        try:
            self._response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return self._response


    def sendDocument(self, chat_id, document, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files={
        'document': open(document, 'rb')
        }
        try:
            self._response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return self._response


    def sendVideo(self,chat_id, video, **kwargs):
        data = {
        'chat_id': chat_id,
        'duration': kwargs.get('duration', None),
        'caption': kwargs.get('caption', None),
        'width': kwargs.get('width', None),
        'height': kwargs.get('height', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files= {
        'video': open(video, 'rb')
        }
        try:
            self._response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return self._response


    def sendVoice(self, chat_id, voice, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'duration': kwargs.get('duration', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files={
        'voice': open(voice, 'rb')
        }
        try:
            self._response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return self._response


    def sendVideoNote(self, chat_id, vnote, **kwargs):
        data = {
        'chat_id': chat_id,
        'duration': kwargs.get('duration', 10),
        'length': kwargs.get('length', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files = {
        'video_note': open(vnote, 'rb')
        }
        try:
            self._response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return self._response


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
        """
        Type of action to broadcast. Choose one, depending on what the user is
        about to receive: typing for text messages, upload_photo for photos,
        record_video or upload_video for videos, record_audio or upload_audio
        for audio files, upload_document for general files, find_location for
        location data, record_video_note or upload_video_note for video notes.
        """
        data = {
        'chat_id': chat_id,
        'action': action
        }
        try:
            self._response = requests.post(self._url + 'sendChatAction',
                                           data=data)
        except:
            return False
        else:
            return self._response


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
