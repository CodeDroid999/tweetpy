client = MongoClient(mongod_connect)
db = client.tweetstream # use or create a database named demo
tweet_collection = db.tweet_trump #use or create a collection named tweet_trump
tweet_collection = db.tweet_biden #use or create a collection named tweet_biden
tweet_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique

