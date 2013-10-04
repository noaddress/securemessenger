import urllib2
import sys
user=sys.argv[1]
url='http://noaddress.x10.mx/chat/'
url+= user
url+=".txt"
response = urllib2.urlopen(url).read()
response=response[4:]

#RSA

def split(txt, seps):
    default_sep = seps[0]
    for sep in seps[1:]: # we skip seps[0] because that's the default seperator
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

response=split(response, ['&', '%26'])
for i in range(0,len(response)):
  print(response[i])
