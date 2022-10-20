stream_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
stream_auth.set_access_token(OAUTH_TOKEN, OATH_TOKEN_SECRET)

strem_api = tweepy.API(stream_auth)

track = ['election'] # define the keywords, tweets contain election

locations = [-78.9326449,38.4150904,-78.8816972,38.4450731] #defin the location, in Harrisonburg, VA

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print (status.id_str)
        try:
            tweet_collection.insert_one(status._json)
        except:
            pass
  
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = strem_api.auth, listener=myStreamListener)
myStream.filter(track=track)#  (locations = locations)   #Use either track or locations

#Authorize the REST API
rest_auth = twitter.oauth.OAuth(OAUTH_TOKEN,OATH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
rest_api = twitter.Twitter(auth=rest_auth)

def on_response(response:tweepy.StreamResponse):
    tweet:tweepy.Tweet = response.data
    users:list = response.includes.get("users") 
    # response.includes is a dictionary representing all the fields (user_fields, media_fields, etc)
    # response.includes["users"] is a list of `tweepy.User`
    # the first user in the list is the author (at least from what I've tested)
    # the rest of the users in that list are anyone who is mentioned in the tweet
    
    author_username = users and users[0].username
    print(tweet.text, author_username)

streaming_client = tweepy.StreamingClient(bearer_token)
streaming_client.on_response = on_response
streaming_client.sample(threaded=True, user_fields = ["id", "name", "username"]) # using user fields 

time.sleep(DURATION)
streaming_client.disconnect()
