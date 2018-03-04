#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

class JsonEnc:
    """
    Doc for class
    """
    def enjson(self):
        raise NotImplementedError


class JsonDec:
    """
    """
    @classmethod
    def dejson(cls, jtype):
        raise NotImplementedError

    @staticmethod
    def check_json(jtype):
        if type(jtype) == dict:
            return jtype
        elif type(jtype) == str:
            return json.loads(jtype)
        else:
            raise ValueError('jtype is not json dict or string type.')


class Update(JsonDec):
    """
    Doc string for Update class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        update_id = obj['update_id']
        if 'message' in obj:
            message = Message.dejson(obj['message'])
        else:
            message = None
        if 'edited_message' in obj:
            edited_message = Message.dejson(obj['edited_message'])
        else:
            edited_message = None
        if 'chanel_post' in obj:
            chanel_post = Message.dejson(obj['chanel_post'])
        else:
            chanel_post = None
        if 'edited_chanel_post' in obj:
            edited_chanel_post = Message.dejson(obj['edited_chanel_post'])
        else:
            edited_chanel_post = None
        if 'inline_query' in obj:
            inline_query = InlineQuery.dejson(obj['inline_query'])
        else:
            inline_query = None
        if 'chosen_inline_result' in obj:
            chosen_inline_result = ChosenInlineResult.dejson(obj['chosen_inline_result'])
        else:
            chosen_inline_result = None
        if 'callback_query' in obj:
            callback_query = CallbackQuery.dejson(obj['callback_query'])
        else:
            callback_query = None
        if 'shipping_query' in obj:
            shipping_query = ShippingQuery.dejson(obj['shipping_query'])
        else:
            shipping_query = None
        if 'pre_checkout_query' in obj:
            pre_checkout_query = PreCheckoutQuery.dejson(obj['pre_checkout_query'])
        else:
            pre_checkout_query = None
        return cls(update_id, message, edited_message, chanel_post,
                   edited_chanel_post, inline_query, chosen_inline_result,
                   callback_query, shipping_query, pre_checkout_query)

    def __init__(self, update_id, message, edited_message, chanel_post,
                 edited_chanel_post, inline_query, chosen_inline_result,
                 callback_query, shipping_query, pre_checkout_query):
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.chanel_post = chanel_post
        self.edited_chanel_post = edited_chanel_post
        self.inline_query = inline_query
        self.chosen_inline_result =chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query


class Message(JsonDec):
    """
    Doc string for Message class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        message_id = obj['message_id']
        if 'from' in obj:
            from_user = User.dejson(obj['from'])
        else:
            from_user = None
        date = obj['date']
        chat = Chat.dejson(obj['chat'])
        options = {}
        if 'forward_from' in obj:
            options['forward_from'] = User.dejson(obj['forward_from'])
        if 'forward_from_chat' in obj:
            options['forward_from_chat'] = Chat.dejson(obj['forward_from_chat'])
        if 'forward_from_message_id' in obj:
            options['forward_from_message_id'] = obj.get('forward_from_message_id')
        if 'forward_signature' in obj:
            options['forward_signature'] = obj.get('forward_signature')
        if 'forward_date' in obj:
            options['forward_date'] = obj.get('forward_date')
        if 'reply_to_message' in obj:
            options['reply_to_message'] = Message.dejson(obj['reply_to_message'])
        if 'edit_date' in obj:
            options['edit_date'] = obj.get('edit_date')
        if 'media_group_id' in obj:
            options['media_group_id'] = obj.get('media_group_id')
        if 'author_signature' in obj:
            options['author_signature'] = obj.get('author_signature')
        if 'text' in obj:
            options['text'] = obj.get('text')
        if 'entities' i obj:
            options['entities'] = []
            for e in obj.get('entities'):
                options['entities'].append(MessageEntity.dejson(e))
        if 'caption_entities' in obj:
            options['caption_entities'] = []
            for ce in obj.get('caption_entities'):
                options['caption_entities'].append(MessageEntity.dejson(ce))
        if 'audio' in obj:
            options['audio'] = Audio.dejson(obj['audio'])
        if 'document' in obj:
            options['document'] = Document.dejson(obj['document'])
        if 'game' in obj:
            options['game'] = Game.dejson(obj['game'])
        if 'photo' in obj:
            options['photo'] = Photo.dejson(obj['photo'])
        if 'sticker' in obj:
            options['sticker'] = Stiker.dejson(obj['stiker'])
        if 'video' in obj:
            options['video'] = Video.dejson(obj['video'])
        if 'voice' in obj:
            options['voice'] = Voice.dejson(obj['voice'])
        if 'video_note' in obj:
            options['video_note'] = VideoNote.dejson(obj['video_note'])
        if 'caption' in obj:
            options['caption'] = obj.get('caption')
        if 'contact' in obj:
            options['contact'] = Contact.dejson(obj['contact'])
        if 'location' in obj:
            options['location'] = Location.dejson(obj['location'])
        if 'venue' in obj:
            options['venue'] = Venue.dejson(obj['venue'])
        if 'new_chat_members' in obj:
            options['new_chat_members'] = []
            for nm in obj.get('new_chat_members'):
                options['new_chat_members'].append(User.dejson(nm))
        if 'left_chat_member' in obj:
            options['left_chat_member'] = User.dejson(obj['left_chat_member'])
        if 'new_chat_title' in obj:
            options['new_chat_title'] = obj.get('new_chat_title')
        if 'new_chat_photo' in obj:
            options['new_chat_photo'] = []
            for photo in obj.get('new_chat_photo'):
                options['new_chat_photo'].append(PhotoSize.dejson(photo))
        if 'delete_chat_photo' in obj:
            options['delete_chat_photo'] = obj.get('delete_chat_photo')
        if 'group_chat_created' in obj:
            options['group_chat_created'] = obj.get('group_chat_created')
        if 'supergroup_chat_created' in obj:
            options['supergroup_chat_created'] = obj.get('supergroup_chat_created')
        if 'channel_chat_created' in obj:
            options['channel_chat_created'] = obj.get('channel_chat_created')
        if 'migrate_to_chat_id' in obj:
            options['migrate_to_chat_id'] = obj.get('migrate_to_chat_id')
        if 'migrate_from_chat_id' in obj:
            options['migrate_from_chat_id'] = obj.get('migrate_from_chat_id')
        if 'pinned_message' in obj:
            options['pinned_message'] = Message.dejson(obj['pinned_message'])
        if 'invoice' in obj:
            options['invoice'] = Invoice.dejson(obj['invoice'])
        if 'successful_payment' in obj:
            options['successful_payment'] = SuccessfulPayment.dejson(obj['successful_payment'])
        if 'connected_website' in obj:
            options['connected_website'] = obj.get('connected_website')
        return cls(message_id, from_user, date, chat, options)

    def __init__(self, message_id, from_user, date, chat, options):
        self.message_id = message_id
        self.from_user = from_user
        self.date = date
        self.chat = chat

        for key in options:
            setattr(self, key, options[key])


class MessageEntity(JsonDec):
    """
    Doc string for MessageEnity class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        ent_type = obj['type']
        offset = obj['offset']
        length = obj['length']
        url = obj.get('url')
        user = None
        if 'user' in obj:
            user = User.dejson(obj['user'])
        return cls(ent_type, offset, length, url, user)


    def __init__(self, etype, offset, length, url=None, user=None):
        self.type = etype
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user

class User(JsonDec):
    """
    Doc string for User class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        uid = obj['id']
        is_bot = obj['is_bot']
        first_name = obj['first_name']
        last_name = obj['last_name']
        username = obj['username']
        language_code = obj['language_code']
        return cls(uid, is_bot, first_name, last_name, username, language_code)

    def __init__(self, uid, is_bot, fname, lname=None, username=None, lang_code=None):
        self.id = uid
        self.is_bot = is_bot
        self.first_name = fname
        self.last_name = lname
        self.username = username
        self.language_code = lang_code


class Chat(JsonDec):
    """
    Doc string for Chat class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        id = obj['id']
        type = obj['type']
        title = obj.get('title')
        username = obj.get('username')
        first_name = obj.get('first_name')
        last_name = obj.get('last_name')
        all_members_are_administrators = obj.get('all_members_are_administrators')
        photo = None
        if 'photo' in obj:
            photo = ChatPhoto.dejson(obj['photo'])
        description = obj.get('description')
        invite_link = obj.get('invite_link')
        pinned_message = None
        if 'pinned_message' in obj:
            pinned_message = Message.dejson(obj['pinned_message'])
        sticker_set_name = obj.get('sticker_set_name')
        can_set_sticker_set = obj.get('can_set_sticker_set')
        return cls(id, type, title, username, first_name, last_name,
                   all_members_are_administrators, photo, description,
                   invite_link, pinned_message, sticker_set_name,
                   can_set_sticker_set)

    def __init__(self, id, type, title=None, username=None, first_name=None,
                 last_name=None,all_members_are_administrators=None, photo=None,
                 description=None, invite_link=None, pinned_message=None,
                 sticker_set_name=None, can_set_sticker_set=None):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.all_members_are_administrators = all_members_are_administrators
        self.photo = photo
        self.description = description
        self. invite_link = invite_link
        self.pinned_message = pinned_message
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set


class PhotoSize(JsonDec):
    """
    Doc for PhotoSize
    """
    @classmethod
    def dejson(cls, jtype):
        obj = clt.check_json(jtype)
        file_id = obj['file_id']
        width = obj['width']
        height = obj['height']
        file_size = obj.get('file_size')
        return cls(file_id, width, height, file_size)

    def __init__(self, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size


class Audio(JsonDec):
    """
    Doc for Audio
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        duration = obj['duration']
        performer = obj.get('performer')
        title = obj.get('title')
        mime_type = obj.get('mime_type')
        file_size = obj.get('file_size')
        return cls(file_id, duration, performer, title, mime_type, file_size)

    def __init__(self, file_id, duration, performer=None, title=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size


class Document(JsonDec):
    """
    Doc for Document class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        thumb = None
        if 'thumb' in obj:
            thumb = PhotoSize.dejson(obj['thumb'])
        file_name = obj.get('file_name')
        mime_type = obj.get('file_name')
        file_size = obj.get('file_size')
        return cls(file_id, thumb, file_name, mime_type, file_size)

    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None
                 file_size=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Video(JsonDec):
    """
    Doc for Video class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        width = obj['width']
        height = obj['height']
        duration = obj['duration']
        thumb = None
        if 'thumb' in obj:
            thumb = PhotoSize.dejson(obj['thumb'])
        mime_type = obj.get('mime_type')
        file_size = obj.get('file_size')
        return cls(file_id, width, height, duration, thumb, mime_type,
                   file_size)

    def __init__(self, file_id, width, height, duration, thumb=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size



class Voice(JsonDec):
    """
    Doc for Voice class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        duration = obj['duration']
        mime_type = obj.get('mime_type')
        file_size = obj.get('file_size')

        return cls(file_id, duration, mime_type, file_size)

    def __init__(self, file_id, duration, mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


class VideoNote(JsonDec):
    """
    Doc for VideoNote class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        length = obj['length']
        duration = obj['duration']
        thumb = None
        if 'thumb' in obj:
            thumb = PhotoSize.dejson(obj['thumb'])
        file_size = obj.get('file_size')
        return cls(file_id, length, duration, thumb, file_size)

    def __init__(self, file_id, length, duration, thumb=None, file_size=None):
        self.file_id = file_id
        self.length = length
        self.duration = duration
        self.thumb = thumb
        self.file_size = file_size


class Contact(JsonDec):
    """
    Doc for Contact class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        phone_number = obj['phone_number']
        first_name = obj['first_name']
        last_name = obj.get('last_name')
        user_id = obj.get('user_id')
        return cls(phone_number, first_name, last_name, user_id)

    def __init__(self, phone_number, first_name, last_name=None, user_id=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id


class InlineQuery(JsonDec):
    """
    """
    def __init__(self):
        pass


class ChosenInlineResult(JsonDec):
    """
    """
    def __init__(self):
        pass


class CallbackQuery(JsonDec):
    """
    """
    def __init__(self):
        pass


class ShippingQuery(JsonDec):
    def __init__(self):
        pass


class PreCheckoutQuery(JsonDec):
    def __init__(self):
        pass
