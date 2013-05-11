# -*- coding: utf-8 -*-

import tweepy
from tweepy.utils import parse_datetime
import os
import re

consumer_key = ''
consumer_secret = ''

access_token_key = ''
access_token_secret = ''

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)

fileName = ''
domainName = ''

fileName = raw_input("Enter the file name : ")
domainName = raw_input("Enter the domain (Enter comma separated domains or simply press return for random tweets.) : ")

if os.path.exists(fileName):
    n = open(fileName,'r+')
    print "Using \"",fileName,"\" which already exists"
else:
    n = open(fileName,'w')
    print "File \"",fileName,"\" is created"


class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        n.write(tweet.text.encode('utf-8') + "\n")

    #def on_data(self, data):
        #n.write(data)

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l)
if not domainName :
    print "No domain name"
    streamer.sample()
else:
    setTerms = [domainName]
    streamer.filter(track = setTerms)
