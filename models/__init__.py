# -*- coding: utf-8 -*-

from mongokit import Connection,Document,ObjectId
import datetime

HOST = 'localhost'
DATABASE = 'shingeki'

conn = Connection(HOST)
database = conn[DATABASE]

@conn.register
class User(Document):
    structure = {
        'created' : datetime.datetime,
        'modified' : datetime.datetime,
        'screen_name' : unicode,
        'profile_image_url' : unicode,
        'name' : unicode,
    }
    default_values = {
        'created' : datetime.datetime.now,
        'modified' : datetime.datetime.now,
    }
    @classmethod
    def get_user(cls,id):
        return users.find_one({'_id':ObjectId(id)})

@conn.register
class Character(Document):
    structure = {
        'created' : datetime.datetime,
        'modified' : datetime.datetime,
        'nick_name' : unicode,
        'search_name' : unicode,
        'full_name' : unicode,
        'profile_text' : unicode,
        'profile_image_url' : unicode,
        'comment' : dict,
        'comment_number': int,
        'vote_number' : int,
    }
    default_values = {
        'created' : datetime.datetime.now,
        'modified' : datetime.datetime.now,
        'vote_number' : 0,
        'comment_number' : 0,
    }

    @classmethod
    def get_character(cls,id):
        return characters.find_one({'_id':ObjectId(id)})

@conn.register
class Tweet(Document):
    structure = {
        'created' : datetime.datetime,
        'modified' : datetime.datetime,
        'character' : Character,
        'user' : User,
        'created_at' : datetime.datetime,
        'source' : unicode,
        'text' : unicode,
    }
    default_values = {
        'created' : datetime.datetime.now,
        'modified' : datetime.datetime.now,
    }
    use_autorefs = True

    @classmethod
    def get_tweet(cls,id):
        return tweets.find_one({'_id':ObjectId(id)})

characters = database['characters']
#character = characters.Character()
#character['nick_name'] =u'mikasa'
#character.save()

users = database['users']
#user = users.User()
#user['name'] = u'ymizushi'
#user.save()

tweets = database['tweets']
#tweet = tweets.Tweet()
#tweet['text'] = u'text'
#tweet['user'] = user
#tweet['character'] = character
#tweet.save()
