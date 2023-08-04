import urllib.request as urllib2
for line in urllib2.urlopen("http://codingseekho.in/APP/vspi.txt"):
    print (line)
