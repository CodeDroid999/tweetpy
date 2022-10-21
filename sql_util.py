import pandas as pd

df=pd.read_json("file.json",orient='columns')
rows = []
for i,r in df.iterrows():
    rows.append({'eventid':i+1,'timemillis':r['events']['timemillis'],'name':r['events']['name']})
df = pd.DataFrame(rows)
print(df)


