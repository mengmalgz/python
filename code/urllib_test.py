import urllib2
 
response = urllib2.urlopen("https://www.toutiao.com/")
print response.read()
