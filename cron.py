# -*- coding: utf-8 -*-

from security_setting import *
import twitter
import models

api = twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)

users = api.GetFollowers()
twi_tweets


for twi_user in users:
    



    if not models.users.find_one({'screen_name':twi_user.screen_name}):
        user = models.users.User()
        print twi_user
        print user
        print twi_user.screen_name
        user['screen_name'] = twi_user.screen_name
        user.save()
