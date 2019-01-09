"""The Main TelegramBot class is here.

all code are here.
"""
import requests
import bot.ttypes as ttypes


class TelBotClass():
    """Documentation for TelBotClass."""

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
        if not response.json()['ok']:
            return
        return response.json()

    def getUpdates(self, **kwargs):
        """Get new incoming messages from bot"""
        self._offset = kwargs.get('offset')
        self._timeout = kwargs.get('timeout')
        self._limit = kwargs.get('limit')

        data = {'offset': self._offset,
                'limit': self._limit,
                'timeout': self._timeout}
        response = self._make_request(method='post',
                                      method_name='/getUpdates',
                                      data=data)
        updates = [ttypes.Update.dejson(resp) for resp in response]
        return updates

    def setWebhook(self, url, **kwargs):
        """Documentation for setWebhook method"""
        data = {'url': url,
                'max_connections': kwargs.get('max_connections', 40),
                'allowed_updates': kwargs.get('allowed_updates')}
        if 'certificate' in list(kwargs.keys()):
            cert = {'certificate': open(kwargs['certificate'], 'rb')}
        else:
            cert = None
        response = self._make_request(method='post',
                                      method_name='/setWebhook',
                                      data=data,
                                      files=cert)
        return response

    def deleteWebhook(self):
        """Try to delete Webhook.
        If success returns True, else returns False"""
        response = self._make_request(method_name='/deleteWebhook')
        return response

    def getWebhookInfo(self):
        """Get information about webhook"""
        response = self._make_request(method_name='/getWebhookInfo')
        wh = ttypes.WebHookInfo.dejson(response)
        return wh

    def sendMessage(self, chat_id, text, **kwargs):
        """ Sending a message from the bot to the specified chat """
        param = {'chat_id': chat_id,
                 'text': text,
                 'parse_mode': kwargs.get('parse_mode'),
                 'disable_web_page_preview':
                     kwargs.get('disable_web_page_preview'),
                 'disable_notification':
                     kwargs.get('disable_notification', False),
                 'reply_to_message_id': kwargs.get('reply_to_message_id'),
                 'reply_markup': kwargs.get('reply_markup')}

        response = self._make_request(method='post',
                                      method_name='/sendMessage',
                                      data=param)
        return ttypes.Message.dejson(response)

    def forwardMessage(self, chat_id, from_chat_id,
                       message_id, disable_notification=True):
        data = {'chat_id': chat_id,
                'from_chat_id': from_chat_id,
                'message_id': message_id,
                'disable_notification': disable_notification}
        response = self._make_request(method='post',
                                      method_name='/forwardMessage',
                                      data=data)
        return ttypes.Message.dejson(response)

    def sendPhoto(self, chat_id, photo, **kwargs):
        data = {'chat_id': chat_id,
                'caption': kwargs.get('caption'),
                'disable_notification':
                    kwargs.get('disable_notification', False),
                'reply_to_message_id': kwargs.get('reply_to_message_id'),
                'reply_markup': kwargs.get('reply_markup')}
        files = {'photo': open(photo, 'rb')}
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
        return ttypes.Message.dejson(response)

    def sendAudio(self, chat_id, audio, **kwargs):
        data = {'chat_id': chat_id,
                'caption': kwargs.get('caption'),
                'duration': kwargs.get('duration'),
                'performer': kwargs.get('performer'),
                'title': kwargs.get('title'),
                'disable_notification':
                    kwargs.get('disable_notification', False),
                'reply_to_message_id': kwargs.get('reply_to_message_id'),
                'reply_markup': kwargs.get('reply_markup')}
        files = {'audio': open(audio, 'rb')}
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
        return ttypes.Message.dejson(response)

    def sendDocument(self, chat_id, document, **kwargs):
        data = {'chat_id': chat_id,
                'caption': kwargs.get('caption'),
                'disable_notification':
                    kwargs.get('disable_notification', False),
                'reply_to_message_id': kwargs.get('reply_to_message_id'),
                'reply_markup': kwargs.get('reply_markup')}
        files = {
            'document': open(document, 'rb')
        }
        response = self._make_request(method='post',
                                      method_name='/sendDocument',
                                      data=data,
                                      files=files)
        return ttypes.Message.dejson(response)

    def sendVideo(self, chat_id, video, **kwargs):
        data = {
            'chat_id': chat_id,
            'duration': kwargs.get('duration'),
            'caption': kwargs.get('caption'),
            'width': kwargs.get('width'),
            'height': kwargs.get('height'),
            'disable_notification': kwargs.get('disable_notification', False),
            'reply_to_message_id': kwargs.get('reply_to_message_id'),
            'reply_markup': kwargs.get('reply_markup')
        }
        files = {
            'video': open(video, 'rb')
        }
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
        return ttypes.Message.dejson(response)

    def sendVoice(self, chat_id, voice, **kwargs):
        data = {
            'chat_id': chat_id,
            'caption': kwargs.get('caption'),
            'duration': kwargs.get('duration'),
            'disable_notification': kwargs.get('disable_notification', False),
            'reply_to_message_id': kwargs.get('reply_to_message_id'),
            'reply_markup': kwargs.get('reply_markup')
        }
        files = {
            'voice': open(voice, 'rb')
        }
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
        return ttypes.Message.dejson(response)

    def sendVideoNote(self, chat_id, vnote, **kwargs):
        data = {
            'chat_id': chat_id,
            'duration': kwargs.get('duration', 10),
            'length': kwargs.get('length'),
            'disable_notification': kwargs.get('disable_notification', False),
            'reply_to_message_id': kwargs.get('reply_to_message_id'),
            'reply_markup': kwargs.get('reply_markup')
        }
        files = {
            'video_note': open(vnote, 'rb')
        }
        response = self._make_request(method='post',
                                      method_name='/sendPhoto',
                                      data=data,
                                      files=files)
        return ttypes.Message.dejson(response)

    def sendMediaGroup(self, chat_id, media,
                       reply_to_message_id=None, **kwargs):
        data = {
            'chat_id': chat_id,
            'disable_notification': kwargs.get('disable_notification', False),
            'reply_to_message_id': reply_to_message_id,
        }
        return

    def sendLocation(self, chat_id, latitude, longtitude, **kwargs):
        data = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longtitude': longtitude,
            'live_period': kwargs.get('live_period', 86400),
            'disable_notification': kwargs.get('disable_notification', False),
            'reply_to_message_id': kwargs.get('reply_to_message_id'),
            'reply_markup': kwargs.get('reply_markup')
        }
        response = self._make_request(method='post',
                                      method_name='/sendLocation',
                                      data=data)
        return rttypes.Message.dejson(response)

    def editMessageLiveLocation(self, chat_id, latitude, longtitude, **kwargs):
        pass

    def stopMessageLiveLocation(self, chat_id=None, message_id=None,
                                inline_message_id=None, reply_markup=None):
        data = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'reply_markup': reply_markup
        }
        response = self._make_request(method='post',
                                      method_name='/stopMessageLiveLocation',
                                      data=data)
        return response

    def sendVenue(self, chat_id, latitude, longtitude, title, address,
                  **kwargs):
        data = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longtitude': longtitude,
            'title': title,
            'address': address,
            'foursquare_id': kwargs.get('foursquare_id'),
            'disable_notification': kwargs.get('disable_notification', False),
            'reply_to_message_id': kwargs.get('reply_to_message_id'),
            'reply_markup': kwargs.get('reply_markup')
        }
        response = self._make_request(method='post', method_name='sendVenue',
                                      data=data)
        return response

    def sendContact(self, chat_id, phone_num, first_name, **kwargs):
        data = {
            'chat_id': chat_id,
            'phone_number': phone_num,
            'first_name': first_name,
            'last_name': kwargs.get('last_name'),
            'disable_notification': kwargs.get('disable_notification', False),
            'reply_to_message_id': kwargs.get('reply_to_message_id'),
            'reply_markup': kwargs.get('reply_markup')
        }
        response = self._make_request(method='post', method_name='sendContact',
                                      data=data)
        return response

    def sendChatAction(self, chat_id, action):
        """
        Type of action to broadcast. Choose one, depending on what the user is
        about to receive.

        :param action: typing, upload_photo, record_video, upload_video,
        record_audio, upload_audio, upload_document, find_location,
        record_video_note, upload_video_note.
        """
        data = {
            'chat_id': chat_id,
            'action': action
        }
        response = self._make_request(method='post',
                                      method_name='/sendChatAction',
                                      data=data)
        return response

    def getUserProfilePhotos(self, user_id, offset, limit):
        data = {
            'user_id': user_id,
            'offset': offset,
            'limit': limit
        }
        response = self._make_request(method='post',
                                      method_name='/getUserProfilePhotos',
                                      data=data)
        return response

    def kickChatMember(self, chat_id, user_id, until_date=None):
        data = {
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
            'until_date': kwargs.get('until_date'),
            'can_send_messages': kwargs.get('can_send_messages', False),
            'can_send_media_messages':
                kwargs.get('can_send_media_messages', False),
            'can_send_other_messages':
                kwargs.get('can_send_other_messages', False),
            'can_add_web_page_previews':
                kwargs.get('can_add_web_page_previews', False)
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
        data = {'chat_id': chat_id}
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
            'chat_id': chat_id,
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
            if ('can_set_sticker_set' in list(chat.keys())
                    and chat['can_set_sticker_set'] is True):
                response = self._make_request(method='post',
                                              method_name='/setChatStickerSet',
                                              data=data)
                return response

    def deleteChatStickerSet(self, chat_id):
        if self.getChat(chat_id):
            chat = self.getChat(chat_id)
            if ('can_set_sticker_set' in list(chat.keys())
                    and chat['can_set_sticker_set'] is True):
                response = self._make_request(
                    method='post',
                    method_name='/deleteChatStickerSet',
                    data={'chat_id': chat_id})
                return response

    def answerCallbackQuery(self, callback_query_id, **kwargs):
        data = {
            'callback_query_id': callback_query_id,
            'text': kwargs.get('text'),
            'show_alert': kwargs.get('show_alert'),
            'url': kwargs.get('url'),
            'cache_time': kwargs.get('cache_time')
        }
        response = self._make_request(method='post',
                                      method_name='/answerCallbackQuery',
                                      data=data)
        return response

    def answerInlineQuery(inline_query_id, results, **kwargs):
        data = {
            'inline_query_id': inline_query_id,
            'results': results,
            'cache_time': kwargs.get('cache_time'),
            'is_personal': kwargs.get('is_personal'),
            'next_offset': kwargs.get('next_offset'),
            'switch_pm_text': kwargs.get('switch_pm_text'),
            'switch_pm_parameter': kwargs.get('switch_pm_parameter')
        }
        response = self._make_request(method='post',
                                      method_name='/answerInlineQuery',
                                      data=data)
        return response

    def editMessageText(self, text, **kwargs):
        data = {
            'chat_id': kwargs.get('chat_id'),
            'message_id': kwargs.get('message_id'),
            'inline_message_id': kwargs.get('inline_message_id'),
            'text': text,
            'parse_mode': kwargs.get('parse_mode'),
            'disable_web_page_preview':
                kwargs.get('disable_web_page_preview', False),
            'reply_markup': kwargs.get('reply_markup')
        }
        response = self._make_request(method='post',
                                      method_name='/editMessageText',
                                      data=data)
        return response

    def editMessageCaption(self, **kwargs):
        data = {
            'chat_id': kwargs.get('chat_id'),
            'message_id': kwargs.get('message_id'),
            'inline_message_id': kwargs.get('inline_message_id'),
            'caption': kwargs.get('caption'),
            'parse_mode': kwargs.get('parse_mode'),
            'reply_markup': kwargs.get('reply_markup')
        }
        response = self._make_request(method='post',
                                      method_name='/editMessageCaption',
                                      data=data)
        return response

    def editMessageReplyMarkup(self, **kwargs):
        data = {
            'chat_id': kwargs.get('chat_id'),
            'message_id': kwargs.get('message_id'),
            'inline_message_id': kwargs.get('inline_message_id'),
            'reply_markup': kwargs.get('reply_markup')
        }
        response = self._make_request(method='post',
                                      method_name='/editMessageReplyMarkup',
                                      data=data)
        return response

    def deleteMessage(self, chat_id, message_id):
        data = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        response = self._make_request(method='post',
                                      method_name='/deleteMessage',
                                      data=data)
        return response
