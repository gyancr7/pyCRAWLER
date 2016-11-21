#!/usr/bin/env python2
import cgi,cgitb
import requests
from google import search
from bs4 import BeautifulSoup
print "Content-Type: text/html\n\n"
form=cgi.FieldStorage()
list=[]
term=form["qer"].value#raw_input('enter the query: ')
number=form["nol"].value#input('enter number of links: ')
#(int)number
for url in search(term,lang='en',stop=5):
        #print(url)
	list.append(url)

print "<html>"
print "<div>"
print "<h1 style='color:white; text-align:center; font-size:50px'>pyCRAWLER</h2>"
print "</div  >"
print "<body style='background-color:black' background='13cd35bdf2e9aba57e53655977efda9b.jpg'>"
print "<div>"
print "<h3 style='color:white'>Top",number,"links for",term,":</h3>"
#for i in range(0,int(number)):
#	lnk =(list[i])
#	print "<a href=",lnk,">",lnk,"<br/></a><form action='linkv.py' method='get'><input type='submit' name='lnk' value=",lnk,"></form>"

for i in range(0,int(number)):
	lnk =(list[i])
	print "<a href=",lnk,">",lnk,"<br/></a><form action='linkv.py' method='get'><input type='submit' name='lk' value=",lnk,"></form>"

print "</div>"

print "<div style='color:white'>"
print "<br/><h3 style='color:white'>Optimized search result for",term,":</h3>"
for j in range(0,int(number)):
	lnkk=(list[j])
	#print "<a href=",lnkk,">",lnkk,"<br/></a>"
	source_code=requests.get(lnkk)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	for link in soup.findAll('p'):
		#link.encode('ascii', '\u2019')
		#print (link)
		text=link.string
		#none='None'
		if (text):
			print "<p style='font-family:Tahoma'><b>",text,"</b></p>"
print"</div>"


print "<br/><br/><br/><h3 style='color:white'>Select any link.</h3>"
print "</body>"
print "</html>"
        #source_code=requests.get(list[i])
	#plain_text=source_code.text
	#soup=BeautifulSoup(plain_text,"lxml")
	#print soup.get_text()
