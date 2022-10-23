#import libraries and functions
import tweepy
import configparse
import CONSUMER_KEY
import CONSUMER_SECRET
import OAUTH_TOKEN
import OATH_TOKEN_SECRET
import tweet_collection




stream_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
stream_auth.set_access_token(OAUTH_TOKEN, OATH_TOKEN_SECRET)

#connect to the tweepy API server
stream_api = tweepy.API(stream_auth)

# define the keywords, tweets that contain the keywords
track = ['election' 'DonaldTrump''trump''biden''trumpVsBiden''republican-in-name-only'
           'Joebiden''election2016''america-decides''the-great-meme-war''race-traitor'
           'cuckservative''presidential-election']  
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print (status.id_str)
        try:
            tweet_collection.insert_one(status._json) #on error
        except:
            pass
  
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = stream_api.auth, listener=myStreamListener)
myStream.filter(track=track)    #Use either track or locations

