# -*- coding: utf-8 -*-

from flask import Flask,request
from flask import render_template
import models

app = Flask(__name__)

@app.route('/')
def get_index():
    values = None
    return render_template('index.html',values=values)

@app.route('/tweets')
def get_tweets():
    tweets = list()
    for tweet in models.tweets.find():
        tweet['user']=models.database.dereference(tweet['user'])
        tweet['character']=models.database.dereference(tweet['character'])

        tweets.append(tweet)
    values = dict(tweets = tweets)
    return render_template('tweets/index.html',values=values)

@app.route('/tweets/<id>')
def get_tweet(id):
    tweet = models.Tweet.get_tweet(id)
    values = dict(tweet = tweet)
    return render_template('tweets/view.html',values=values)

@app.route('/users')
def get_users():
    users = [user for user in models.users.find()]
    values = dict(users = users)
    return render_template('users/index.html',values=values)

@app.route('/users/<id>')
def get_user(id):
    user = models.User.get_user(id)
    values = dict(user = user)
    return render_template('users/view.html',values=values)

@app.route('/characters')
def get_characters():
    characters = [character for character in models.characters.find()]
    values = dict(characters = characters)
    return render_template('characters/index.html',values=values)

@app.route('/characters/<id>',methods=['GET','POST'])
def get_character(id):
    if request.method =='POST':
        models.Character.update_character(id,{"$push" : {'comment':{'text' : request.form['text']}}})
        #models.Character.update_character(id,{"$set" : {'comment':request.form['text']}})
    character = models.Character.get_character(id)
    values = dict(character = character)
    return render_template('characters/view.html',values=values)

if __name__ == '__main__':
    app.debug = True
    app.run()
