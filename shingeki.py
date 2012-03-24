# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
import models
import time

app = Flask(__name__)

@app.route('/')
def get_index():
    values = dict(hoge = "")
    return render_template('index.html',values=values)

@app.route('/tweets')
def get_tweets():
    tweets = [tweet for tweet in models.Tweets.find()]
    values = dict(tweets = tweets)
    return render_template('tweets/index.html',values=values)

@app.route('/users')
def get_users():
    users = [user for user in models.Users.find()]
    values = dict(users = users)
    return render_template('users/index.html',values=values)

@app.route('/characters')
def get_character():
    characters = [character for character in models.Characters.find()]
    values = dict(characters = characters)
    return render_template('characters/index.html',values=values)

if __name__ == '__main__':
    app.debug = True
    app.run()
