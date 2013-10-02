from Tkinter import *
import urllib2
import threading
import time
user=""
master = Tk()
global me
global n
n=0
me="ttttt"
history=["","","","","","","","","",""]
eu = Entry(master)
eu.pack()

eu.focus_set()
def callbacku():
  global user
  user=eu.get()
print user
bu = Button(master, text="GO", width=10, command=callbacku)
bu.pack()
w = Canvas(master, width=800, height=500)
w.pack()
e = Entry(master)
e.pack()

e.focus_set()

def sendarg(a):
  send()

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

def read():
  while(1==1):
    urlr='http://noaddress.x10.mx/chat/'
    urlr+= me
    urlr+=".txt"
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
    for i in range(0,9):
      history[i]=readtext[len(readtext)-(i+1)]
      print history
     # root = Tk()
   #   label = Label( root, textvariable=history[i], relief=RAISED )
    #  label.pack()    
    time.sleep(2)
    
    
    
def my_inline_function(a):
    #do some stuff
    download_thread = threading.Thread(target=read)
    download_thread.daemon = True
    download_thread.start()
    if (a==1):
        download_thread.stop()
        print "quit"
    return
my_inline_function(n)


  
mainloop()
    