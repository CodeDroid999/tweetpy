



import pymongo
import mongod_connect

#create database stream object
client = MongoClient(mongod_connect)
db = client.tweetstream                   # use or create a database named tweetstream
tweet_collection = db.tweet_trump         #use or create a collection named tweet_trump.json
tweet_collection = db.tweet_biden         #use or create a collection named tweet_biden.json
tweet_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique


#establish connection between local machine and database
from pymongo import MongoClient
client = MongoClient('localhost:27017')

#saves the tweetstream into alltweets.json
def get_document(MyStreamListener):       #get tweetstream from the MystreamListener class
    return {
        'id': post['id_str'], 
        'text': post['text'], 
        'created_at': post['created_at'], 
        'retweet_count' : post['retweet_count'], 
        'favourites_count': post['user']['favourites_count'], 
        'lang': post['lang'],
        'screen_name': post['user']['screen_name'] 
    }

for tweet in result1:
    try:
        tweet_collection.insert(
            get_document(alltweets)        #saving into alltweets.json
        )
    except:
        pass

#search alltweets.json for tweets for each president
def get_document(alltweets):              #searching alltweets.json for tweets for donaldtrump tweets
    return {
        'id': post['trump''donaldtrump''donald''republican''DonaldTrump'], 
        'text': post['text'], 
        'created_at': post['created_at'], 
        'retweet_count' : post['retweet_count'], 
        'favourites_count': post['user']['favourites_count'], 
        'lang': post['lang'],
        'screen_name': post['user']['screen_name'] 
    }
for tweet in result1:
    try:
        tweet_collection.insert(
            get_document(tweet_trump)        #saving donald trump tweets into tweets_trump.json
        )
    except:
        pass

def get_document(alltweets):              #searching alltweets.json for tweets for biden tweets
    return {
        'id': post['biden''joebiden''joe_biden''liberalparty''JoeBiden'], 
        'text': post['text'], 
        'created_at': post['created_at'], 
        'retweet_count' : post['retweet_count'], 
        'favourites_count': post['user']['favourites_count'], 
        'lang': post['lang'],
        'screen_name': post['user']['screen_name'] 
    }
for tweet in result1:
    try:
        tweet_collection.insert(
            get_document(tweet_trump)        #saving joe biden tweets into tweets_biden.json
        )
    except:
        pass
