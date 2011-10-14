#! /usr/bin/env python2.7
from twitter_app import Application
from gmail import gmail
import time

class integrate():
 
  def loop(self): # twitter and gmail are checked periodically
    twitter = Application()
    twitter.initial_twitter()

    gmail_obj = gmail()
    gmail_obj.initial_gmail()
 
    i=1
    while i == 1:
         twitter.loop()
         time.sleep(2)
         twitter.check_messages()
         time.sleep(2)
         twitter.check_mentions()
         time.sleep(2)
         gmail_obj.check_mails()
         time.sleep(2)  

