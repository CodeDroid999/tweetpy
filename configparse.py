import configparser


config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY      = config['mytwitter']['api_key']        #replace with actual api key
CONSUMER_SECRET   = config['mytwitter']['api_secrete']    #replace with actual api secret
OAUTH_TOKEN       = config['mytwitter']['access_token']   #replace with actual access token
OATH_TOKEN_SECRET = config['mytwitter']['access_secrete'] #replace with actual access

#connecting to mongodb
mongod_connect = config['mymongo']['connection']
