import urllib2
import sys
user=sys.argv[1]
text=sys.argv[2]
#user = raw_input("USERNAME: ")
#text = raw_input("TEXT: ")


#RSA

url='http://noaddress.x10.mx/chat/index.php?user='
url+= user
url+="&text="
url+=text
response = urllib2.urlopen(url)
html = response.read() 
