
import pandas as pd
import tweet_collection

#open JSON files from the local machine 
df=pd.read_json("trump_tweets.json",orient='columns')        #open trump_tweets.json and process the data into columns
df=pd.read_json("biden_tweets.json",orient='columns')        #open biden_tweets.json and process the data into columns
rows = []
for i,r in df.iterrows():                            #process the data into rows     
    rows.append({'eventid':i+1,'timemillis':r['events']['timemillis'],'name':r['events']['name']})
df = pd.DataFrame(rows)
print(df)=tweet_collection 


#query collected json data  
def get_document(trump_tweets):#reading json file saved to local machine
    return {
        'id': post['id_str'], 
        'text': post['text'], 
        'created_at': post['created_at'], 
        'retweet_count' : post['retweet_count'], 
        'favourites_count': post['user']['favourites_count'], 
        'lang': post['lang'],
        'screen_name': post['user']['screen_name'] 
    }


 def get_document(biden_tweets):#reading trump_tweets saved to local machine
    return {
        'id': post['id_str'], 
        'text': post['text'], 
        'created_at': post['created_at'], 
        'retweet_count' : post['retweet_count'], 
        'favourites_count': post['user']['favourites_count'], 
        'lang': post['lang'],
        'screen_name': post['user']['screen_name'] 
    }

#saving the queries into sql tables
for tweet in result1:
    try:
        tweet_collection.insert(
            get_document(tweet_trump)#inserting and saving all trump tweets into tweet_trump sql table
        )
    except:
        pass

for tweet in result2:
    try:
        tweet_collection.insert(
            get_document(tweet_biden)#inserting and saving all biden tweets into tweet_biden sql table
        )
    except:
        pass
   
      