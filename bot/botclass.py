
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


class TelBotClass():
    """Documentation for TelBotClass"""
    def __init__(self, token):
        self._token = token
        self._url = "https://api.telegram.org/bot" + self._token

    def _make_request(self, method_name, method='get', **kwargs):
        request_url = self._url + method_name
        response = requests.request(method, request_url, **kwargs)
        return self._check_request(response)['result']

    def _check_request(self, response):
        if response.status_code != 200:
            response.raise_for_status()
        try:
            result_json = response.json()
        except:
            return None # заглушка TODO: допиши норм код!!!
        if not result_json['ok']:
            return
        return result_json

    def getUpdates(self, **kwargs):
        """Get new incoming messages from bot"""
        self._offset = kwargs.get('offset', None)
        self._timeout = kwargs.get('timeout', None)
        self._limit = kwargs.get('limit', None)

        data = {
        'offset': self._offset,
        'limit': self._limit,
        'timeout': self._timeout
        }
        response = self._make_request(method='post',
                                      method_name='/getUpdates',
                                      data=data)
        return response

    def setWebhook(self, url, **kwargs):
        """Documentation for setWebhook method"""
        data={
        'url': url,
        'max_connections': kwargs.get('max_connections', 40),
        'allowed_updates': kwargs.get('allowed_updates', None)
        }
        if 'certificate' in list(kwargs.keys()):
            cert = {
            'certificate': open(kwargs['certificate'], 'rb')
            }
        else:
            cert = None
        response = self._make_request(method='post',
                                      method_name='/setWebhook',
                                      data=data,
                                      files=cert)
        return response


    def deleteWebhook(self):
        """Try to delete Webhook. If success returns True, else returns False"""
        response = self._make_request(method_name='/deleteWebhook')
        return response

    def getWebhookInfo(self):
        """Get information about webhook"""
        response = self._make_request(method_name='/getWebhookInfo')
        return response


    def sendMessage(self, chat_id, text, **kwargs):
        """ Sending a message from the bot to the specified chat """
        param = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': kwargs.get('parse_mode', None),
        'disable_web_page_preview': kwargs.get('disable_web_page_preview',
                                               None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }

        response = self._make_request(method='post',
                                      method_name='/sendMessage',
                                      data=param)
        return response

    def forwardMessage(self, chat_id,from_chat_id,
                       message_id, disable_notification=True):
        data = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'disable_notification': disable_notification
        }
        response = self._make_request(method='post',
                                      method_name='/forwardMessage',
                                      data=data)
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
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
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
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
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
        response = self._make_request(method='post',
                                      method_name='/sendDocument',
                                      data=data,
                                      files=files)
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
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
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
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
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
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
        return response

    def sendMediaGroup(self, chat_id, media,
                       reply_to_message_id=None, **kwargs):
        data = {
        'chat_id': chat_id,
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': reply_to_message_id,
        }
        pass

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
        response = self._make_request(method='post',
                                      method_name='/sendLocation',
                                      data=data)
        return response

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
        response = self._make_request(method='post',
                                      method_name='/sendChatAction',
                                      data=data)
        return response

    def getUserProfilePhotos(self, user_id, **kwargs):
        pass

    def kickChatMember(self, chat_id, user_id, until_date=None):
        data= {
        'chat_id': chat_id,
        'user_id': user_id,
        'until_date': until_date
        }
        response = self._make_request(method='post',
                                      method_name='/kickChatMember',
                                      data=data)
        return response

    def unbanChatMember(self, chat_id, user_id):
        data = {
        'chat_id': chat_id,
        'user_id': user_id
        }
        response = self._make_request(method='post',
                                      method_name='/unbanChatMember',
                                      data=data)
        return response

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
        response = self._make_request(method='post',
                                      method_name='/restrictChatMember',
                                      data=data)
        return response


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
        response = self._make_request(method='post',
                                      method_name='/promoteChatMember',
                                      data=data)
        return response

    def exportChatInviteLink(self, chat_id):
        data={'chat_id': chat_id}
        response = self._make_request(method='post',
                                      method_name='/exportChatInviteLink',
                                      data=data)
        return response

    def setChatPhoto(self, chat_id, chat_photo):
        data = {
        'chat_id': chat_id
        }
        files = {
        'photo': open(chat_photo, 'rb')
        }
        response = self._make_request(method='post',
                                      method_name='/setChatPhoto',
                                      data=data,
                                      files=files)
        return response

    def deleteChatPhoto(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        response = self._make_request(method='post',
                                      method_name='/deleteChatPhoto',
                                      data=data)
        return response

    def setChatTitle(self, chat_id, title):
        data = {
        'chat_id': chat_id,
        'title': title
        }
        response = self._make_request(method='post',
                                      method_name='/setChatTitle',
                                      data=data)
        return response

    def setChatDescription(self, chat_id, description):
        data = {
        'chat_id': chat_id,
        'description': str(description)
        }
        response = self._make_request(method='post',
                                      method_name='/setChatDescription',
                                      data=data)
        return response

    def pinChatMessage(self, chat_id, message_id,
                       disable_notification=False):
        data = {
        'chat_id':chat_id,
        'message_id': message_id,
        'disable_notification': disable_notification
        }
        response = self._make_request(method='post',
                                      method_name='/pinChatMessage',
                                      data=data)
        return response

    def unpinChatMessage(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        response = self._make_request(method='post',
                                      method_name='/unpinChatMessage',
                                      data=data)
        return response

    def leaveChat(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        response = self._make_request(method='post',
                                      method_name='/leaveChat',
                                      data=data)
        return response

    def getChat(self, chat_id):
        response = self._make_request(method='post',
                                      method_name='/getChat',
                                      data={'chat_id': chat_id})
        return response

    def getChatAdministrators(self, chat_id):
        response = self._make_request(method='post',
                                      method_name='/getChatAdministrators',
                                      data={'chat_id': chat_id})
        return response

    def getChatMembersCount(self, chat_id):
        response = self._make_request(method='post',
                                      method_name='/getChatMembersCount',
                                      data={'chat_id': chat_id})
        return response

    def getChatMember(self, chat_id, member_id):
        data = {
        'chat_id': chat_id,
        'member_id': int(member_id)
        }
        response = self._make_request(method='post',
                                      method_name='/getChatMember',
                                      data=data)
        return response

    def setChatStickerSet(self, chat_id, sticker_set_name):
        data = {
        'chat_id': chat_id,
        'sticker_set_name': sticker_set_name
        }
        if self.getChat(chat_id):
            chat = self.getChat(chat_id)
            if ('can_set_sticker_set' in list(chat.keys()) and
                chat['can_set_sticker_set'] == True):
                response = self._make_request(method='post',
                                              method_name='/setChatStickerSet',
                                              data=data)
                return response

    def deleteChatStickerSet(self, chat_id):
        if self.getChat(chat_id):
            chat = self.getChat(chat_id)
            if ('can_set_sticker_set' in list(chat.keys()) and
                chat['can_set_sticker_set'] == True):
                response = self._make_request(method='post',
                                              method_name='/deleteChatStickerSet',
                                              data={'chat_id': chat_id})
                return response


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
        data = {
        'chat_id': chat_id,
        'message_id': message_id
        }
        response = self._make_request(method='post',
                                      method_name='/deleteMessage',
                                      data=data)
        return response
