import sys
import urllib2

response = urllib2.urlopen('http://localhost:5000')
print response.read()
