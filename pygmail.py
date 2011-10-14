#! /usr/bin/env python2.7
import imaplib,re

class pygmail:

  file1 = open('username.txt','r')
  username = file1.read()
  file2 = open('password.txt','r')
  password = file2.read()
  GMAIL_IMAP_SERVER = 'imap.gmail.com'
  GMAIL_IMAP_PORT = '993'
  GMAIL_USERNAME = username
  GMAIL_PASSWORD = password

  def __init__(self): 
     self.conn = imaplib.IMAP4_SSL(self.GMAIL_IMAP_SERVER,self.GMAIL_IMAP_PORT)

  def login(self):
     rc,self.response = self.conn.login(self.GMAIL_USERNAME,self.GMAIL_PASSWORD)

  def logout(self):
     self.conn.logout()

  def get_mail_count(self,folder='Inbox'):
     rc,count = self.M.select(folder)
     return count[0]

  def get_unread_count(self):
     unreadCount = re.search"UNSEEN (\d+)", self.conn.status("INBOX", "(UNSEEN)")[1][0]).group(1)
     return unreadCount

