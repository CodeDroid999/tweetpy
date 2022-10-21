
import pandas as pd
import tweet_collection

#open JSON files from the MongoDB database and 
df=pd.read_json("file.json",orient='columns')        #process the data into columns
rows = []
for i,r in df.iterrows():                            #process the data into rows     
    rows.append({'eventid':i+1,'timemillis':r['events']['timemillis'],'name':r['events']['name']})
df = pd.DataFrame(rows)
print(df)  #print the data into NOSQL tables


#query collected data in MongoDB
 
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