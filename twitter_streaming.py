# -*- coding: utf-8 -*-
"""
Twitter streaming file from http://adilmoujahid.com/posts/2014/07/twitter-analytics/

"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
with open('/Users/scjacob/OneDrive - Capgemini/DS&A/Mabe/Demo Development/twitter_keys.json', 'rb') as f:
        keychain = json.load(f)
        access_token = keychain['access_token']
        access_token_secret = keychain['access_token_secret']
        consumer_key = keychain['consumer_key']
        consumer_secret = keychain['consumer_secret']

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['refrigerator'])
    print ('Currently Running')
    
    
"""
run the below line in the terminal. Will pipe output in json format to file. Manually need to stop with ctrl+c
python twitter_streaming.py > twitter_data.json
"""