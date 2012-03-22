from pymongo import Connection

conn = Connection('localhost')
tweets = conn['shingeki']['tweets']


