# -*- coding: iso-8859-15 -*-
from Tkinter import *
import urllib2
import threading
import time
user=""
master = Tk()
master.wm_title("SecureMessenger-UNENCRYPTED")
global me
global n
global urlr
global l1
global l2
global l3
global l4
global l5
global l6
global l7
global l8
global l9
global l10

global myname
showstarttext=1



n=0
me=""
history=["","","","","","","","","",""]
w = Canvas(master, width=800, height=500)
w.pack()

def callbacku():
  global user
  user=eu.get()
  return
#print user
bu = Button(master, text="Connect to:", width=10, command=callbacku)
bu.pack()
bu.place(x=20, y=20)

eu = Entry(master)
eu.pack()

eu.place(x=150, y=25)

em = Entry(master)
em.pack()
em.place(x=485, y=25)
em.focus_set()
em.destroy()
def loe():
  a=0
def read(*me):
  while(1==1):
    urlr='http://noaddress.x10.mx/chat/'
    global myname
    myname=''
    for i in range(0,len(me)):
      myname+= me[i]
      urlr+= me[i]
    urlr+=".txt"
    #print urlr

    response = urllib2.urlopen(urlr).read()
    #response=response[4:]  
    def split(txt, seps):
      default_sep = seps[0]
      for sep in seps[1:]: # we skip seps[0] because that's the default seperator
	  txt = txt.replace(sep, default_sep)
      return [i.strip() for i in txt.split(default_sep)]
    response=split(response, ['&', '%26'])
    readtext=response
    
    
    #RSA
    
    
    x=9
    if (len(readtext)<=9):
      x=len(readtext)
    for i in range(0,x):
      history[i]=readtext[len(readtext)-(i+1)]

    print history
    #print readtext
    l1.config(text=history[8])
    l2.config(text=history[7])
    l3.config(text=history[6])
    l4.config(text=history[5])
    l5.config(text=history[4])
    l6.config(text=history[3])
    l7.config(text=history[2])
    l8.config(text=history[1])
    l9.config(text=history[0])
    l10.destroy()
    if (len(readtext)%10==0):
      clear()

    time.sleep(2)


  
def callbackme():
  me=el.get()
  masterlogin.destroy()
  download_thread = threading.Thread(target=read,args=me)
  download_thread.daemon = True
  download_thread.start()
  em.destroy()
  bm.destroy()
  loggedin = Label(master, text="Logged in as:"+myname)
  loggedin.pack()
  loggedin.place(x=485, y=25)
  eu.focus_set()
  l1 = Label(master, text="")
  l1.pack()
  l1.place(x=300, y=200)
  l2 = Label(master, text="")
  l2.pack()
  l2.place(x=300, y=220)
  l3 = Label(master, text="")
  l3.pack()
  l3.place(x=300, y=240)
  l4 = Label(master, text="")
  l4.pack()
  l4.place(x=300, y=260)
  l5 = Label(master, text="")
  l5.pack()
  l5.place(x=300, y=280)
  l6 = Label(master, text="")
  l6.pack()
  l6.place(x=300, y=300)
  l7 = Label(master, text="")
  l7.pack()
  l7.place(x=300, y=320)
  l8 = Label(master, text="")
  l8.pack()
  l8.place(x=300, y=340)
  l9 = Label(master, text="")
  l9.pack()
  l9.place(x=300, y=360)
  l10 = Label(master, text="")
  l10.pack()
  l10.place(x=300, y=380)
  e.focus_set()

def loginscreen():
  global masterlogin
  masterlogin = Tk()
  masterlogin.wm_title("LOGIN SecureMessenger")
  wlogin = Canvas(masterlogin, width=520, height=400)
  wlogin.pack()
  logintext = Label(masterlogin, text="RULES:\n\n1) Remember your username!\n2) NEVER use special characters\n3) Only the last 10 messages are saved on the server\n4) Enter your friends username in top left corner before writing\n5) Your messages are NOT encrypted\n6) Your computer only stores last 10 messages after terminating the program\n7) Never do stupid things\n\n\n\n\nPlesase enter your Username to login.")
  logintext.pack()
  logintext.place(x=20, y=20)
  bl = Button(masterlogin, text="Login", width=10, command=callbackme)
  bl.pack()
  bl.place(x=350, y=350)
  global el
  el = Entry(masterlogin)
  el.pack()
  el.place(x=150, y=355)
  masterlogin.focus_set()
  el.focus_set()
  masterlogin.wm_attributes("-topmost", 1)
  masterlogin.focus()
  
if(showstarttext==1):
  loginscreen()
  showstarttext=0
#print me
bm = Button(master, text="Login FIRST!", width=10, command=loe)
bm.pack()
bm.place(x=670, y=20)


e = Entry(master)
e.pack()


def sendarg(*a):
  send(me)
  return

def clear():
    url='http://noaddress.x10.mx/chat/index.php?user='
    url+= user
    url+="&text=content-deleted"
    response = urllib2.urlopen(url)
    html = response.read() 
    return



def send(*me):
  text=e.get()
  print myname
  text=text.replace(' ', '+')
 # text=text.replace('ä', 'ae')
 # text=text.replace('ö', 'oe')
 # text=text.replace('ü', 'ue')
 


  print text
  e.delete(0, END)
  url='http://noaddress.x10.mx/chat/index.php?user='
  url+= user
  url+="&text="
  url+=myname
  url+=":"
  url+=text
  print url
  response = urllib2.urlopen(url)
  html = response.read() 
  
e.bind('<Return>', sendarg)
b = Button(master, text="send", width=10, command=sendarg)
b.pack()

    
def my_inline_function(a):
    #do some stuff
    download_thread = threading.Thread(target=read)
    download_thread.daemon = True
    download_thread.start()
    return
def about():
  masterabout = Tk()
  masterabout.wm_title("About SecureMessenger")
  wabout = Canvas(masterabout, width=600, height=350)
  wabout.pack()
  license = Label(masterabout, text="The MIT License (MIT)\n\nCopyright (c) 2013 noaddress, lolralf\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of\nthis software and associated documentation files (the \"Software\"), to deal in\nthe Software without restriction, including without limitation the rights to\nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of\nthe Software, and to permit persons to whom the Software is furnished to do so,\nsubject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\nFOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER\nIN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n")
  license.pack()
  license.place(x=20, y=20)


babout = Button(master, text="about", width=10, command=about)
babout.pack()
babout.place(x=670, y=515)

mainloop()
    