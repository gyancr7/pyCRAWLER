#!/usr/bin/env python2
import cgi,cgitb
import requests
from google import search
from bs4 import BeautifulSoup
print "Content-Type: text/html\n\n"
print "<h1 style='color:white; text-align:center; font-size:50px'>pyCRAWLER</h2><br/>"
print "<body style='background-color:black' background='13cd35bdf2e9aba57e53655977efda9b.jpg'>"
print "<a href='samhtml.html' style='font-size:30px;font-color:magenta;'>Back to Home</a>"
form=cgi.FieldStorage()
lnkk=form["lk"].value
print "<br/><h3 style='color:white;font-size:30px'>The selected link is: </h3><a style='color:green;font-size:25px' href=",lnkk,">",lnkk,"</a>"
source_code=requests.get(lnkk)
plain_text=source_code.text
print "<br/><h3 style='color:white'>Recursive Links:</h3>"
soup=BeautifulSoup(plain_text)
for link in soup.findAll('a'):
	#link.encode('ascii', '\u2019')
	#print (link)
	text=link.string
	#none='None'
	if (text):
		l=lnkk+"/"+text
		print "<a href=",l,">",l,"<br/></a><form action='linkv.py' method='get'><input type='submit' name='lk' value=",l,"></form>"
