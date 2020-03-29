#!/usr/bin/python36

import cgi
import subprocess as sp
print("content-type: text/html")
print()

a=cgi.FieldStorage()
l1=a.keys()
f = open('/etc/ansible/abc','w+')
f.write('[lb]')
f.write('\n')
f.write('[webserver]')
f.write('\n')

for i in range(len(l1)):

	f.write(str(a.getvalue(l1[i])))
	f.write('\n')
f.close()
print("Success")
