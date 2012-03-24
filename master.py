# -*- coding: utf-8 -*-
from models import *

characters_structure = [
    {
        'created' : str(),
        'modified' : str(),
        'nick_name' : 'mikasa',
        'search_name' : u'ミカサ',
        'first_name_en' : str(),
        'last_name_en' : str(),
        'first_name_jp' : str(),
        'last_name_jp' : str(),
        'profile_text' : str(),
        'vote_number' : int(),
    }
]

Characters.set(characters_structure)
Characters.insert()
