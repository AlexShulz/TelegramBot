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

        response = requests.post(self._url
                                       + '/sendMessage', data=param)
        return response

    def forwardMessage(self, chat_id,from_chat_id,
                       message_id, disable_notification=True):
        data = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'disable_notification': disable_notification
        }
        try:
            response = requests.post(self._url + '/forwardMessage',
                                           data=data)
        except:
            return None
        else:
            return response

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
            response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return response

    def sendAudio(self, chat_id, audio, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'duration': kwargs.get('duration', None),
        'performer': kwargs.get('performer', None),
        'title': kwargs.get('title', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files = {
        'audio': open(audio, 'rb')
        }
        try:
            response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return response

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
            response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return response

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
            response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return response

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
            response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return response

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
            response = requests.post(self._url + '/sendPhoto',
                                           data=data, files=files)
        except:
            return None
        else:
            return response

    def sendMediaGroup(self, chat_id, media,
                       reply_to_message_id=None, **kwargs):
        data = {
        'chat_id': chat_id,
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': reply_to_message_id,
        }

    def sendLocation(self, chat_id, latitude, longtitude, **kwargs):
        data = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longtitude': longtitude,
        'live_period': kwargs.get('live_period', 86400),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        try:
            response = requests.post(self._url + '/sendLocation', data=data)
        except:
            return None
        else:
            return response.json()['result']

    def editMessageLiveLocation(self, chat_id, latitude, longtitude, **kwargs):
        pass

    def stopMessageLiveLocation(self, chat_id, **kwargs):
        pass

    def sendVenue(self, chat_id, latitude, longtitude, title, address, **kwargs):
        pass

    def sendContact(self, chat_id, phone_num, first_name, **kwargs):
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
            response = requests.post(self._url + '/sendChatAction',
                                           data=data)
        except:
            return False
        else:
            return True

    def getUserProfilePhotos(self, user_id, **kwargs):
        pass

    def kickChatMember(self, chat_id, user_id, until_date=None):
        data= {
        'chat_id': chat_id,
        'user_id': user_id,
        'until_date': until_date
        }
        try:
            requests.post(self._url + '/kickChatMember', data=data)
        except:
            return False
        else:
            return True

    def unbanChatMember(self, chat_id, user_id):
        data = {
        'chat_id': chat_id,
        'user_id': user_id
        }
        try:
            requests.post(self._url + '/unbanChatMember', data=data)
        except:
            return False
        else:
            return True

    def restrictChatMember(self, chat_id, user_id, **kwargs):
        data = {
        'chat_id': chat_id,
        'user_id': user_id,
        'until_date': kwargs.get('until_date', None),
        'can_send_messages': kwargs.get('can_send_messages', False),
        'can_send_media_messages': kwargs.get('can_send_media_messages', False),
        'can_send_other_messages': kwargs.get('can_send_other_messages', False),
        'can_add_web_page_previews': kwargs.get('can_add_web_page_previews',
                                                False)
        }
        try:
            requests.post(self._url + '/restrictChatMember', data=data)
        except:
            return False
        else:
            return True

    def promoteChatMember(self, chat_id, user_id, **kwargs):
        data = {
        'chat_id': chat_id,
        'user_id': user_id,
        'can_change_info': kwargs.get('can_change_info', True),
        'can_post_messages': kwargs.get('can_post_messages', True),
        'can_edit_messages': kwargs.get('can_edit_messages', True),
        'can_delete_messages': kwargs.get('can_delete_messages', True),
        'can_invite_users': kwargs.get('can_invite_users', True),
        'can_restrict_members': kwargs.get('can_restrict_members', True),
        'can_pin_messages': kwargs.get('can_pin_messages', True),
        'can_promote_members': kwargs.get('can_promote_members', True)
        }
        try:
            requests.post(self._url + '/promoteChatMember', data=data)
        except:
            return False
        else:
            return True

    def exportChatInviteLink(self, chat_id):
        try:
            response = requests.post(self._url + '/exportChatInviteLink',
                                     data={'chat_id': chat_id})
        except:
            return None
        else:
            return response.json()['result']

    def setChatPhoto(self, chat_id, chat_photo):
        data = {
        'chat_id': chat_id
        }
        files = {
        'photo': open(chat_photo, 'rb')
        }
        try:
            response = requests.post(self._url + '/setChatPhoto',
                                           data=data, files=files)
        except:
            return False
        else:
            return True

    def deleteChatPhoto(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        try:
            requests.post(self._url + '/deleteChatPhoto', data=data)
        except:
            return False
        else:
            return True

    def setChatTitle(self, chat_id, title):
        data = {
        'chat_id': chat_id,
        'title': title
        }
        try:
            requests.post(self._url + '/setChatTitle', data=data)
        except:
            return False
        else:
            return True

    def setChatDescription(self, chat_id, description):
        data = {
        'chat_id': chat_id,
        'description': str(description)
        }
        try:
            requests.post(self._url + '/setChatDescription', data=data)
        except:
            return False
        else:
            return True

    def pinChatMessage(self, chat_id, message_id,
                       disable_notification=False):
        data = {
        'chat_id':chat_id,
        'message_id': message_id,
        'disable_notification': disable_notification
        }
        try:
            requests.post(self._url + '/pinChatMessage', data=data)
        except:
            return False
        else:
            return True

    def unpinChatMessage(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        try:
            requests.post(self._url + '/unpinChatMessage', data=data)
        except:
            return False
        else:
            return True

    def leaveChat(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        try:
            requests.post(self._url + '/leaveChat', data=data)
        except:
            return False
        else:
            return True

    def getChat(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        try:
            response = requests.post(self._url + '/getChat', data=data)
        except:
            return None
        else:
            return response.json()['result']

    def getChatAdministrators(self, chat_id):
        try:
            response = requests.post(self._url + '/getChatAdministrators',
                          data={'chat_id': chat_id})
        except:
            return None
        else:
            return response.json()['result']

    def getChatMembersCount(self, chat_id):
        try:
            response = requests.post(self._url + '/getChatMembersCount',
                                     data={'chat_id': chat_id})
        except:
            return None
        else:
            return response.json()["result"]

    def getChatMember(self, chat_id, member_id):
        data = {
        'chat_id': chat_id,
        'member_id': int(member_id)
        }
        try:
            response = requests.post(self._url + '/getChatMember',data=data)
        except:
            return None
        else:
            response.json()['result']

    def setChatStickerSet(self, chat_id, sticker_set_name):
        data = {
        'chat_id': chat_id,
        'sticker_set_name': sticker_set_name
        }
        if self.getChat(chat_id):
            chat = self.getChat(chat_id)
            if ('can_set_sticker_set' in list(chat.keys()) and
                chat['can_set_sticker_set'] == True):
                try:
                    requests.post(self._url + '/setChatStickerSet', data=data)
                except:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def deleteChatStickerSet(self, chat_id):
        if self.getChat(chat_id):
            chat = self.getChat(chat_id)
            if ('can_set_sticker_set' in list(chat.keys()) and
                chat['can_set_sticker_set'] == True):
                try:
                    requests.post(self._url + '/deleteChatStickerSet',
                                  data={'chat_id': chat_id})
                except:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def answerCallbackQuery(self, callback_query_id, **kwargs):
        pass

    def answerInlineQuery(inline_query_id, results, **kwargs):
        pass

    def editMessageText(self, text, **kwargs):
        pass

    def editMessageCaption(self, **kwargs):
        pass

    def editMessageReplyMarkup(self, **kwargs):
        pass

    def deleteMessage(self, chat_id, message_id):
        try:
            requests.post(self._url + '/deleteMessage',
                          data = {'chat_id': chat_id,'message_id': message_id})
        except:
            return False
        else:
            return True
