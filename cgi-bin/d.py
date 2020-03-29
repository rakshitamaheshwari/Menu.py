#!/usr/bin/python36

import subprocess


print("content-type: text/html")
print()


x = subprocess.getoutput("sudo docker images")

print("<form action='http://192.168.43.44/cgi-bin/docker.py'>")
print("enter ur docker name : ")
print("<input name='n' />")

print("<br />")

print("Enter ur image name : ")
print("<select name='img'>")


for   i  in  x.split("\n")[1:]:
	j = i.split()
	print("<option>" +  j[0] +  ":"  + j[1] +  "</option>")



print("</select>")


print("<input type='submit' />")


print("</form>")
