#!/usr/bin/env python
import tweepy
import time
import serial
import Tkinter

# files are opened and the access key \& token are retrieved
file1 = open('access_key.txt','r')
file2 = open('access_secret.txt','r')
key = file1.read()
secret = file2.read()
file1.close()
file2.close()

CONSUMER_KEY = '58aNDZrTXYBT7ykDVHpIXg'
CONSUMER_SECRET = 'afSrpK2bnty2oQt1jjgVafLR6SM7ZPWiSXwqScHE'
ACCESS_KEY = key
ACCESS_SECRET = secret
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

class Application:

  def check_messages(self): # twitter is checked for any new messages  
     while self.last_msgCount <  self.msgCount:
       msg = self.messages[0]
       print 'new message'
       print msg.text       # the new message is printed
       self.ser = serial.Serial('/dev/ttyACM0',9600)
       self.ser.write(str('twittermsg')) #'twittermsg' is sent to serial port(arduino)which lights LED
       self.last_msgCount += 1
       time.sleep(5)
       print 'turn off LED'
       self.ser = serial.Serial('/dev/ttyACM0',9600)
       self.ser.write(str('5')) # '5' is sent to serial port to turn off LED
       time.sleep(2)    
	
  def check_mentions(self): # twitter is checked for any new mentions 
     while self.last_mentionsCount < self.mentionsCount:
       mention = self.mentions[0]  
       print "you've been  mentioned"
       print mention.text
       ser = serial.Serial('/dev/ttyACM0',9600)
       ser.write(str('twittermn'))
       self.last_mentionsCount+= 1
       time.sleep(5)
       print 'turn off LED'
       self.ser = serial.Serial('/dev/ttyACM0',9600)
       self.ser.write(str('6'))
       time.sleep(2)

  def loop(self): # count of no. of messages and mentions is updated 
     msgCount = 0
     mentionsCount = 0
     self.messages = api.direct_messages()
     self.mentions = api.mentions()
     self.msgCount = len(self.messages) - 1
     self.mentionsCount = len(self.mentions) - 1

  def initial_twitter(self): # message and mention counts are initiated
     messages = api.direct_messages()
     mentions = api.mentions()
     msgCount = len(messages) - 1
     mentionsCount = len(mentions) - 1
     self.last_msgCount=msgCount
     self.last_mentionsCount=mentionsCount

