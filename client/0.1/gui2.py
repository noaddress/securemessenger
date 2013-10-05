# -*- coding: iso-8859-15 -*-
import mtTkinter as Tkinter #thanks to Allen B. Taylor, a dot b dot taylor at gmail dot com, http://tkinter.unpythonic.net/wiki/mtTkinter
from mtTkinter import * #thanks to Allen B. Taylor, a dot b dot taylor at gmail dot com, http://tkinter.unpythonic.net/wiki/mtTkinter
import urllib2
import threading
import time
global masterlogin
global master
global masterabout
global buttonnewuser
global l1, l2, l3, l4, l5, l6, l7, l8, l9, w, myname, showlogin
showlogin=1




def read(*me):
  while(1==1):
    urlr='http://noaddress.x10.mx/chat/'
    global myname
    global history
    history=['','','','','','','','','','']
    myname=''
    for i in range(0,len(me)):
      myname+= me[i]
      urlr+= me[i]
    urlr+=".txt"
    response = urllib2.urlopen(urlr).read()
    #response=response[4:]  
    def split(txt, seps):
      default_sep = seps[0]
      for sep in seps[1:]:
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
    l1.config(text=history[8])
    l2.config(text=history[7])
    l3.config(text=history[6])
    l4.config(text=history[5])
    l5.config(text=history[4])
    l6.config(text=history[3])
    l7.config(text=history[2])
    l8.config(text=history[1])
    l9.config(text=history[0])
    #print history
    #if (len(readtext)%10==0):
    #  clear()
    time.sleep(2)
    


def clear():
    global myname
    url='http://noaddress.x10.mx/chat/index.php?user='
    url+= myname
    url+="&text=content-deleted"
    response = urllib2.urlopen(url)
    html = response.read() 
    return    
    


def startclient():
  global l1, l2, l3, l4, l5, l6, l7, l8, l9, w, myname
  w = Canvas(master, width=800, height=500)
  w.pack()
  def callbacku():
    global user
    user=entryuser.get()
    return
  buttonuser = Button(master, text="Connect to:", width=10, command=callbacku)
  buttonuser.pack()
  buttonuser.place(x=20, y=20)
  entryuser = Entry(master)
  entryuser.pack()
  entryuser.place(x=150, y=25)
  babout = Button(master, text="about", width=10, command=about)
  babout.pack()
  babout.place(x=670, y=450)
  l1 = Label(master, text="")
  l1.pack()
  l1.place(x=200, y=200)
  l2 = Label(master, text="")
  l2.pack()
  l2.place(x=200, y=220)
  l3 = Label(master, text="")
  l3.pack()
  l3.place(x=200, y=240)
  l4 = Label(master, text="")
  l4.pack()
  l4.place(x=200, y=260)
  l5 = Label(master, text="")
  l5.pack()
  l5.place(x=200, y=280)
  l6 = Label(master, text="")
  l6.pack()
  l6.place(x=200, y=300)
  l7 = Label(master, text="")
  l7.pack()
  l7.place(x=200, y=320)
  l8 = Label(master, text="")
  l8.pack()
  l8.place(x=200, y=340)
  l9 = Label(master, text="")
  l9.pack()
  l9.place(x=200, y=360)
  download_thread = threading.Thread(target=read,args=me)
  download_thread.daemon = True
  download_thread.start()
  #display_thread = threading.Thread(target=display)
  #display_thread.daemon = True
  #display_thread.start()
  loggedin = Label(master, text="Logged in as: "+myname)
  loggedin.pack()
  loggedin.place(x=570, y=25)

  e = Entry(master)
  e.pack()
  e.place(x=200, y=455)
  def send(*ag):
    def send1():
      text=e.get()
      #print myname
      text=text.replace(' ', '+')
      # text=text.replace('ä', 'ae')
    # text=text.replace('ö', 'oe')
    # text=text.replace('ü', 'ue')
    #  print text
      e.delete(0, END)
      url='http://noaddress.x10.mx/chat/index.php?user='
      url+= user
      url+="&text="
      url+=myname
      url+=":"
      url+=text
    # print url
      response = urllib2.urlopen(url)
      html = response.read()  
    send1()
  e.bind('<Return>', send)
  b = Button(master, text="SEND", width=10, command=send)
  b.pack()
  b.place(x=400, y=450)
  bclear = Button(master, text="Clear All", width=10, command=clear)
  bclear.pack()
  bclear.place(x=550, y=450)




def display():
  l1.config(text=history[8])
  l2.config(text=history[7])
  l3.config(text=history[6])
  l4.config(text=history[5])
  l5.config(text=history[4])
  l6.config(text=history[3])
  l7.config(text=history[2])
  l8.config(text=history[1])
  l9.config(text=history[0])


  
  
def about():
  masterabout = Tk()
  masterabout.wm_title("About SecureMessenger")
  wabout = Canvas(masterabout, width=600, height=350)
  wabout.pack()
  masterabout.maxsize(600,350)
  masterabout.minsize(600,350)
  license = Label(masterabout, text="The MIT License (MIT)\n\nCopyright (c) 2013 noaddress, lolralf\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of\nthis software and associated documentation files (the \"Software\"), to deal in\nthe Software without restriction, including without limitation the rights to\nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of\nthe Software, and to permit persons to whom the Software is furnished to do so,\nsubject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\nFOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER\nIN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n")
  license.pack()
  license.place(x=20, y=20)

def login():
  global me, el, masterlogin
  me=el.get()
  masterlogin.destroy()
  global master
  master=Tk()
  master.maxsize(800,500)
  master.minsize(800,500)
  master.wm_title("SecureMessenger-UNENCRYPTED")
  startclient()

def newuser():
  global myname
  myname=el.get()
  clear()
  login()

def loginwindow():
  global showlogin, el, masterlogin
  if(showlogin==1):
    showlogin=0
    masterlogin=Tk()
    masterlogin.wm_title("LOGIN SecureMessenger")
    wlogin = Canvas(masterlogin, width=520, height=400)
    wlogin.pack()
    masterlogin.maxsize(520,400)
    masterlogin.minsize(520,400)
    logintext = Label(masterlogin, text="RULES:\n\n1) Remember your username!\n2) NEVER use special characters\n3) Only the last 10 messages are saved on the server\n4) Enter your friends username in top left corner before writing\n5) Your messages are NOT encrypted\n6) Your computer only stores last 10 messages after terminating the program\n7) Never do stupid things\n\n\n\n\nPlesase enter your Username to login.")
    logintext.pack()
    logintext.place(x=20, y=20)
    bl = Button(masterlogin, text="Login", width=10, command=login)
    bl.pack()
    bl.place(x=250, y=350)
    el = Entry(masterlogin)
    el.pack()
    el.place(x=50, y=355)
    el.focus_set()
    buttonnewuser = Button(masterlogin, text="New User", width=10, command=newuser)
    buttonnewuser.pack()
    buttonnewuser.place(x=400, y=350)
  return
  if(showlogin==0): 
    display()
loginwindow()
mainloop()
  
  