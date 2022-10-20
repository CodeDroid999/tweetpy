#______________________________________________
#   
#    CIS 612 Lab Assignment 3 
#
#        Author: 
#______________________________________________ 

#import libraries
import pymongo
from pymongo import MongoClient
import json
import tweepy
import twitter
from pprint import pprint
import configparser
import pandas as pd
import sys





from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print "hello world"
    #...

t = Timer(secs, hello_world)
t.start()


y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)


from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

def hello_world():
    print "hello world"
    #...

t = Timer(secs, hello_world)
t.start()




'''
OAUTH
'''
CONSUMER_KEY      = "" # fill your oauth
CONSUMER_SECRET   = "" # fill your oauth
OAUTH_TOKEN       = "" # fill your oauth
OATH_TOKEN_SECRET = "" # fill your oauth

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OATH_TOKEN_SECRET)

api = tweepy.API(auth)

'''

define query in Stream API
'''

track = ['election']

locations = [-84.56,33.62,-84.20,33.91]

'''
fetch data
'''

# class MyStreamListener(tweepy.StreamListener):
#   
#     def on_status(self, status):
#         print (status.id_str)
#         try:
#             tweet_collection.insert(status._json)
#         except:
#             pass
#   
#     def on_error(self, status_code):
#         if status_code == 420:
#             #returning False in on_data disconnects the stream
#             return False
#   
# myStreamListener = MyStreamListener()
#   
#   
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#   
#   
# myStream.filter(track=track, locations = locations, async=True)



'''

query collected data in MongoDB
'''
 
tweet_cursor = tweet_collection.find()
    
print (tweet_cursor.count())
    
user_cursor = tweet_collection.distinct("user.id")
    
    
print (len(user_cursor))
   
   
    
for document in tweet_cursor:
    try:
        print ('----')      
#         pprint (document)
 
    
        print ('name:', document["user"]["name"])
        print ('text:', document["text"])
    except:
        print ("***error in encoding")

        pass
#      