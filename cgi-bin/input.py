#!/usr/bin/python36
print("content-type:text/html")
print()
import subprocess as sp
import cgi
form=cgi.FieldStorage()
n=form.getvalue('servers')

print("<body bgcolor='lightgrey'>") 
print("<form action='http://192.168.43.44/cgi-bin/aa.py'>")
for i in range(0,int(n)):
	print("Enter server{}'s ip value: <input name=s{} />".format(i+1,i+1))
	print("<br/>")
print("<input type='submit'/>")
print("</form>")
print("</body>")
