#!/usr/bin/python36
import cgi
print("content-type: text/html")                  #header(to be read by browser)(but does not get printed)
print()                                           #seperate via new line

mydata=cgi.FieldStorage()            
a=mydata.getvalue("u")               # 'u' is name for input tag of username in user.html file

import subprocess as sp
sp.getoutput("docker run -it {}".format(a))
print("docker launched successfully")
