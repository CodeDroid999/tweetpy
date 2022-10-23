
import pandas as pd
import tweet_collection

#open JSON files from the local machine 
df=pd.read_json("trump_tweets.json",orient='columns')        #open trump_tweets.json and process the data into columns
df=pd.read_json("biden_tweets.json",orient='columns')        #open biden_tweets.json and process the data into columns
rows = []
for i,r in df.iterrows():                            #process the data into rows     
 rows.append({'eventid':i+1,'timemillis':r['events']['timemillis'],'name':r['events']['name']})



#query collected json data  
def get_trump(trump_tweets):#reading json file saved to local machine
 
    SELECT 
    ID, 
    Details, 
    JSON_VALUE(details,'$.author_id') AS author,
    JSON_VALUE(details,'$.text') AS text,
    JSON_VALUE(details,'$.history') AS Created_at
    JSON_VALUE(details,'$.history') AS updated_at
FROM tweets_trump.json


CREATE TABLE tweets_trump (
   ...
   Country AS JSON_VALUE(trump_tweets, '$.Country''$.author''$.text''$.created_at''$.updated_at') PERSISTED,
   ...
)

CREATE INDEX IX_ThatTable_Country ON dbo.tweets_trump(author,text,created_at,updated_at)

#reading biden_tweets saved to local machine
 def get_biden(biden_tweets):
      SELECT 
    ID, 
    Details, 
    JSON_VALUE(details,'$.author_id') AS author,
    JSON_VALUE(details,'$.text') AS text,
    JSON_VALUE(details,'$.history') AS Created_at
    JSON_VALUE(details,'$.history') AS updated_at
FROM tweets_trump.json


CREATE TABLE tweets_trump (
   ...
   Country AS JSON_VALUE(biden_tweets, '$.Country''$.author''$.text''$.created_at''$.updated_at') PERSISTED,
   ...
)

CREATE INDEX IX_ThatTable_Country ON dbo.biden_trump(author,text,created_at,updated_at)

#saving the queries into sql tables
for tweet in result1:
    try:
        tweet_collection.insert(
            get_trump(tweet_trump)#inserting and saving all trump tweets into tweet_trump sql table
        )
    except:
        pass

for tweet in result2:
    try:
        tweet_collection.insert(
            get_biden(tweet_biden)#inserting and saving all biden tweets into tweet_biden sql table
        )
    except:
        pass
   
      