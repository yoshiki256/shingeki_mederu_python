# -*- coding: utf-8 -*-

from pymongo import Connection
import time
conn = Connection('localhost')

class Tweets:
    tweets = conn['shingeki']['tweets']
    structure = {
        'created' : str(),
        'modified' : str(),
        'character' : dict(),
        'user' : dict(),
        'created_at' : str(),
        'source' : str(),
        'text' : str(),
    }

    @classmethod
    def find(cls,query=None):
        return cls.tweets.find(query)

    @classmethod
    def get(cls):
        return cls.structure
    
    def put(self):
        tweets.insert(cls.structure)

class Users:
    users = conn['shingeki']['users']
    structure = {
        'created' : time.asctime(),
        'modified' : time.asctime(),
        'screen_name' : str(),
        'profile_image_url' : str(),
        'name' : str(),
    }

    @classmethod
    def find(cls,query=None):
        return cls.users.find(query)

    @classmethod
    def get(cls):
        return cls.structure

    @classmethod
    def insert(self):
        return users.insert(cls.structure)

class Characters:
    characters = conn['shingeki']['characters']
    structure = {
        'created' : str(),
        'modified' : str(),
        'nick_name' : 'mikasa',
        'search_name' : '',
        'first_name_en' : str(),
        'last_name_en' : str(),
        'first_name_jp' : str(),
        'last_name_jp' : str(),
        'profile_text' : str(),
        'vote_number' : int(),
    }

    @classmethod
    def find(cls,query=None):
        return cls.characters.find(query)

    @classmethod
    def get(cls):
        return cls.structure

    @classmethod
    def set(cls,structure):
        cls.structure = structure

    @classmethod
    def insert(cls):
        return cls.characters.insert(cls.structure)
