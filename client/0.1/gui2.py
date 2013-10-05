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
global l1, l2, l3, l4, l5, l6, l7, l8, l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20, w, myname, showlogin,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20
showlogin=1




def read(*me):
  while(1==1):
    urlr='http://noaddress.x10.mx/chat/'
    global myname
    global history
    history=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
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
    
     #print history
   # print readtext
   # print ""
    x=20
    if (len(readtext)<=20):
      x=len(readtext)
    for i in range(0,x):
      history[i]=readtext[len(readtext)-(i+1)]
      q=-2
   # l1.config(text=history[19])
   # l2.config(text=history[18+q])
    l3.config(text=history[17+q])
    l4.config(text=history[16+q])
    l5.config(text=history[15+q])
    l6.config(text=history[14+q])
    l7.config(text=history[13+q])
    l8.config(text=history[12+q])
    l9.config(text=history[11+q]) 
    l10.config(text=history[10+q])
    l11.config(text=history[9+q])
    l12.config(text=history[8+q])
    l13.config(text=history[7+q])
    l14.config(text=history[6+q])
    l15.config(text=history[5+q])
    l16.config(text=history[4+q])
    l17.config(text=history[3+q])
    l18.config(text=history[2+q])
    l19.config(text=history[1+q])
    l20.config(text=history[0+q])
    #print history
    #if (len(readtext)%10==0):
    #  clear()
    time.sleep(2)
    
def readfriend(*me):
  while(1==1):
    urlrf='http://noaddress.x10.mx/chat/friend-'
    global mynamef,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20
    global historyf
    historyf=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    mynamef=''
    for i in range(0,len(me)):
      mynamef+= me[i]
      urlrf+= me[i]
    urlrf+=".txt"
    responsef = urllib2.urlopen(urlrf).read()
    #response=response[4:]  
    def split(txt, seps):
      default_sep = seps[0]
      for sep in seps[1:]:
	  txt = txt.replace(sep, default_sep)
      return [i.strip() for i in txt.split(default_sep)]
    responsef=split(responsef, ['&', '%26'])
    readtextf=responsef
    
    
    #RSA
    
    
    x=17
    if (len(readtextf)<=17):
      x=len(readtextf)
    for i in range(0,x):
      historyf[i]=readtextf[len(readtextf)-(i+1)]
      
    if(x>=1):
      f1.config(text="1) "+historyf[0])
    if(x>=2):
      f2.config(text="2) "+historyf[1])
    if(x>=3):
      f3.config(text="3) "+historyf[2])
    if(x>=4):
      f4.config(text="4) "+historyf[3])
    if(x>=5):
      f5.config(text="5) "+historyf[4])    
    if(x>=6):
      f6.config(text="6) "+historyf[5])
    if(x>=7):
      f7.config(text="7) "+historyf[6])
    if(x>=8):
      f8.config(text="8) "+historyf[7])
    if(x>=9):
      f9.config(text="9) "+historyf[8])    
    if(x>=10):
      f10.config(text="10) "+historyf[9])
    if(x>=11):
      f11.config(text="11) "+historyf[10])
    if(x>=12):
      f12.config(text="12) "+historyf[11])
    if(x>=13):
      f13.config(text="13) "+historyf[12])
    if(x>=14):
      f14.config(text="14) "+historyf[13])
    if(x>=15):
      f15.config(text="15) "+historyf[14])
    if(x>=16):
      f16.config(text="16) "+historyf[15])
    if(x>=17):    
      f17.config(text="17) "+historyf[16])
   # f18.config(text="18) "+historyf[17])
   # f19.config(text="19) "+historyf[18])
   # f20.config(text="20) "+historyf[19])
    #print history
    #if (len(readtext)%10==0):
    #  clear()
    time.sleep(10)    

def clearfriend():
    global myname
    url='http://noaddress.x10.mx/chat/index.php?user=friend-'
    url+= myname
    url+="&text=content-deleted"
    response = urllib2.urlopen(url)
    html = response.read() 
    return   
  
def clear():
    global myname
    url='http://noaddress.x10.mx/chat/index.php?user='
    url+= myname
    url+="&text=content-deleted"
    response = urllib2.urlopen(url)
    html = response.read() 
    return    
    
def addfriend():
  
  def sendfriend():
    friend=eaddf.get()
    #print myname
    friend=friend.replace(' ', '+')
    # text=text.replace('ä', 'ae')
  # text=text.replace('ö', 'oe')
  # text=text.replace('ü', 'ue')
  #  print text
    eaddf.delete(0, END)
    url='http://noaddress.x10.mx/chat/index.php?user=friend-'
    url+= myname
    url+="&text="
    url+=friend
  # print url
    response = urllib2.urlopen(url)
    html = response.read()  
  masterfriend=Tk()
  masterfriend.wm_title("Add Friends-SecureMessenger")
  wfriend = Canvas(masterfriend, width=600, height=350)
  wfriend.pack()
  masterfriend.maxsize(600,350)
  masterfriend.minsize(600,350)
  frtext = Label(masterfriend, text="Manage your Friends here. There's no undo for delete!")
  frtext.pack()
  frtext.place(x=20, y=20)
  labelf = Label(masterfriend, text="Enter your Friend here")
  labelf.pack()
  labelf.place(x=20, y=400)
  eaddf = Entry(masterfriend)
  eaddf.pack()
  eaddf.place(x=200, y=200)
  baddf = Button(masterfriend, text="ADD", width=10, command=sendfriend)
  baddf.pack()
  baddf.place(x=400, y=195)
  eaddf.focus_set()
  bdelf = Button(masterfriend, text="DELETE ALL FRIENDS", width=20, command=clearfriend)
  bdelf.pack()
  bdelf.place(x=365, y=245)
  
def startclient():
  global l1, l2, l3, l4, l5, l6, l7, l8, l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20, w, myname,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20
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
  l1.place(x=200, y=80)
  l2 = Label(master, text="")
  l2.pack()
  l2.place(x=200, y=100)
  l3 = Label(master, text="")
  l3.pack()
  l3.place(x=200, y=120)
  l4 = Label(master, text="")
  l4.pack()
  l4.place(x=200, y=140)
  l5 = Label(master, text="")
  l5.pack()
  l5.place(x=200, y=160)
  l6 = Label(master, text="")
  l6.pack()
  l6.place(x=200, y=180)
  l7 = Label(master, text="")
  l7.pack()
  l7.place(x=200, y=200)
  l8 = Label(master, text="")
  l8.pack()
  l8.place(x=200, y=220)
  l9 = Label(master, text="")
  l9.pack()
  l9.place(x=200, y=240)
  l10 = Label(master, text="")
  l10.pack()
  l10.place(x=200, y=260)
  l11 = Label(master, text="")
  l11.pack()
  l11.place(x=200, y=280)
  l12 = Label(master, text="")
  l12.pack()
  l12.place(x=200, y=300)
  l13 = Label(master, text="")
  l13.pack()
  l13.place(x=200, y=320)
  l14 = Label(master, text="")
  l14.pack()
  l14.place(x=200, y=340)
  l15 = Label(master, text="")
  l15.pack()
  l15.place(x=200, y=360)
  l16 = Label(master, text="")
  l16.pack()
  l16.place(x=200, y=380)
  l17 = Label(master, text="")
  l17.pack()
  l17.place(x=200, y=400)
  l18 = Label(master, text="")
  l18.pack()
  l18.place(x=200, y=420)
  l19 = Label(master, text="")
  l19.pack()
  l19.place(x=200, y=440)
  l20 = Label(master, text="")
  l20.pack()
  l20.place(x=200, y=460)
  
  
  
  f0 = Label(master, text="Known Friends:")
  f0.pack()
  f0.place(x=50, y=80)
  
  f1= Label(master, text="")
  f1.pack()
  f1.place(x=50, y=100)
  f2 = Label(master, text="")
  f2.pack()
  f2.place(x=50, y=120)
  f3 = Label(master, text="")
  f3.pack()
  f3.place(x=50, y=140)
  f4 = Label(master, text="")
  f4.pack()
  f4.place(x=50, y=160)
  f5 = Label(master, text="")
  f5.pack()
  f5.place(x=50, y=180)
  f6 = Label(master, text="")
  f6.pack()
  f6.place(x=50, y=200)
  f7 = Label(master, text="")
  f7.pack()
  f7.place(x=50, y=220)
  f8 = Label(master, text="")
  f8.pack()
  f8.place(x=50, y=240)
  f9 = Label(master, text="")
  f9.pack()
  f9.place(x=50, y=260)
  f10= Label(master, text="")
  f10.pack()
  f10.place(x=50, y=280)
  f11= Label(master, text="")
  f11.pack()
  f11.place(x=50, y=300)
  f12= Label(master, text="")
  f12.pack()
  f12.place(x=50, y=320)
  f13= Label(master, text="")
  f13.pack()
  f13.place(x=50, y=340)
  f14= Label(master, text="")
  f14.pack()
  f14.place(x=50, y=360)
  f15= Label(master, text="")
  f15.pack()
  f15.place(x=50, y=380)
  f16= Label(master, text="")
  f16.pack()
  f16.place(x=50, y=400)
  f17= Label(master, text="")
  f17.pack()
  f17.place(x=50, y=420)
  f18= Label(master, text="")
  f18.pack()
  f18.place(x=50, y=440)
  f19= Label(master, text="")
  f19.pack()
  f19.place(x=50, y=480)
  f20= Label(master, text="")
  f20.pack()
  f20.place(x=50, y=500)

  download_thread = threading.Thread(target=read,args=me)
  download_thread.daemon = True
  download_thread.start()
  display_thread = threading.Thread(target=readfriend, args=me)
  display_thread.daemon = True
  display_thread.start()
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
  bclear = Button(master, text="Clear Chat", width=10, command=clear)
  bclear.pack()
  bclear.place(x=550, y=450)
  bclear = Button(master, text="Manage Friends", width=10, command=addfriend)
  bclear.pack()
  bclear.place(x=20, y=450)




  
  
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
  
  