#! /usr/bin/env python2.7
from pygmail import pygmail
import serial
import time
import Tkinter

handler = pygmail()
handler.login()

class gmail:
  
  def initial_gmail(self): 
     unread_emails = int(handler.get_unread_count())
     self.last_gmailcount = unread_emails

  def check_mails(self): 
     unread_emails = int(handler.get_unread_count())
     while self.last_gmailcount < unread_emails:
       print "you've got mail"
       ser = serial.Serial('/dev/ttyACM0',9600)
       ser.write(str('gmail'))
       self.last_gmailcount += 1
       time.sleep(5)
       print 'turn off light '
       ser = serial.Serial('/dev/ttyACM0',9600)
       ser.write(str('4'))
       time.sleep(2)

