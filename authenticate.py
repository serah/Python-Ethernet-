#! /usr/bin/env python2.7

import tweepy
import Tkinter
import tkSimpleDialog
import webbrowser

class authentication:
  
  def __init__(self,master): #initiates the gui window
    frame = Tkinter.Frame(master)
    frame.pack()
  
    self.pincode = Tkinter.Button(frame,text = 'Authenticate twitter account',command = self.get_access)
    self.pincode.pack()

    self.gmail = Tkinter.Button(frame,text = 'Register gmail user',command = self.gmail)
    self.gmail.pack()

    self.usefile = Tkinter.Button(frame,text ='start application',command = self.work)
    self.usefile.pack()  
    
  
  def get_access(self): # authenticates the twitter app, gets the access key & token and saves them 
    CONSUMER_KEY = 'consumer key'
    CONSUMER_SECRET = 'consumer secret'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth_url = auth.get_authorization_url()
    
    webbrowser.open(auth_url)

    pin = tkSimpleDialog.askstring(root,'enter the pin')
    verifier = pin.strip()
    auth.get_access_token(verifier)
    key = auth.access_token.key
    secret = auth.access_token.secret

    file1 = open("access_key.txt","w")
    file1.write(key)
    file1.close()
    file2 = open("access_secret.txt','w')
    file2.write(secret)
    file2.close()     


  def gmail(self): # asks for email id and password and saves them 
    userName = tkSimpleDialog.askstring(root,'enter email id')
    password = tkSimpleDialog.askstring(root,'enter password') 
    
    file1 = open('username.txt','w')
    file1.write(userName)
    file2 = open('password.txt','w')
    file2.write(password)
  
    self.enable_imap()


  def enable_imap(self): # Gives instructions on how imap is to be enabled 
    site = webbrowser.open('http://www.gmail.com')
   
    new = Tkinter.Toplevel() 
    instructions = Tkinter.Text(new,state = 'normal',width=100,height=8,bg = 'black',
    fg = 'DarkOliveGreen',font = 'Times')
    instructions.grid()
    instructions.insert('end',"INSTRUCTIONS TO ENABLE ACCESS \n 1.Login to gmail \n 2.Click the gear icon in the upper-right and select Gmail settings at the top of any Gmail page. \n 3.Click Forwarding and POP/IMAP. \n 4.Select Enable IMAP. \n 5.click Save Changes.\n 6. If it was already enabled then start application but if it wasn't \n then start application after atleast 5 min")

  def work(self): # calls integrated.py and starts the app
    from integrated import integrate
    obj = integrate()
    obj.loop()

root = Tkinter.Tk()
app = authentication(root)
root.mainloop()
