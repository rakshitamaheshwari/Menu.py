#!/usr/bin/python36
import subprocess as sp
print("content-type: text/html")
print()


a=sp.getoutput("sudo docker ps")
print(a)
