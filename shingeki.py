# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
import models

app = Flask(__name__)
models.tweets.insert({'name': 'mizushima'})

@app.route('/')
def get_index():
    values = dict(hoge = "hoge")
    return render_template('index.html',values=values)

@app.route('/tweets')
def get_tweets():
    tweets = [tweet['name']for tweet in models.tweets.find()]
    values = dict(tweets = tweets)
    return render_template('tweets/index.html',values=values)

if __name__ == '__main__':
    app.debug = True
    app.run()


