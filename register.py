#!/usr/bin/env python2
import sqlite3
import cgi,cgitb
print "Content-Type: text/html\n\n"
form =cgi.FieldStorage()
nam=form["username"].value
passw=form["password"].value
conn=sqlite3.connect('/var/crawl.db')
#print ("connected successfully\n")
print "<h1 style='color:white; text-align:center; font-size:50px'>pyCRAWLER</h2><br/>"
print "<body style='background-color:black' background='13cd35bdf2e9aba57e53655977efda9b.jpg'>"
conn.execute('''create table if not exists hist(uname text,history text)''')
conn.execute('''create table if not exists user(name text primary key not null,password text not null)''')
if((form["selected"].value)=='Register'):
	conn.execute("insert into user values "+"("+"'"+nam+"'"+","+"'"+passw+"'"+");")
	print "<p style='color:green;'>hello",nam,"!</p>"	
	print "<p style='color:blue;'>You have successfully registered!</p>"
	print "<a href='login.html'>Continue to Login</a>"	
	conn.execute("commit;")
	
flag=0

if((form["selected"].value)=='Login'):
	cursor=conn.execute("select password from user where name="+"'"+nam+"'")
	for row in cursor:
		if(row[0]==passw):							
				flag=1
				break
	
	if(flag==1):
		print "<p style='color:green;'>hello",nam,"!</p>"	
		print "<p style='color:blue;'>You have successfully logged in!</p>"
		print "<form action='samhtml.html' method='get'>"
		print "<input type='submit' name='search' value='Search'>"	
	if(flag==0):
		print "<p style='color:red;'>wrong username or password!</p>"
	        print "<a href='login.html'>Try again</a>"
		
conn.close();
