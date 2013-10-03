from Tkinter import *
import urllib2
import threading
import time
user=""
master = Tk()
global me
global n
global urlr
global l1
global l2
global l3
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

l1 = Label(master, text="Please log in")
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



def read(*me):
  while(1==1):
    urlr='http://noaddress.x10.mx/chat/'
    for i in range(0,len(me)):
      urlr+= me[i]
    urlr+=".txt"
    #print urlr

    response = urllib2.urlopen(urlr).read()
    response=response[4:]
  
    #RSA
  
    def split(txt, seps):
      default_sep = seps[0]
      for sep in seps[1:]: # we skip seps[0] because that's the default seperator
	  txt = txt.replace(sep, default_sep)
      return [i.strip() for i in txt.split(default_sep)]
  
    response=split(response, ['&', '%26'])
    readtext=response
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
    
    
    time.sleep(2)



def callbackme():
  me=em.get()
  download_thread = threading.Thread(target=read,args=me)
  download_thread.daemon = True
  download_thread.start()
  eu.focus_set()

  

#print me
bm = Button(master, text="Login", width=10, command=callbackme)
bm.pack()
bm.place(x=670, y=20)


e = Entry(master)
e.pack()

e.focus_set()

def sendarg(a):
  send()
  return

def send():
  text=e.get()
  e.delete(0, END)
  url='http://noaddress.x10.mx/chat/index.php?user='
  url+= user
  url+="&text="
  url+=text
  response = urllib2.urlopen(url)
  html = response.read() 
  
e.bind('<Return>', sendarg)
b = Button(master, text="send", width=10, command=send)
b.pack()

    
def my_inline_function(a):
    #do some stuff
    download_thread = threading.Thread(target=read)
    download_thread.daemon = True
    download_thread.start()
    return

  
mainloop()
    