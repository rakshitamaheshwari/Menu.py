#!/usr/bin/python36

import subprocess as sp
print("content-type: text/html")
print()

#print("<marquee>hello</marquee>")
#cmd= "sudo docker ps"


x="pop"

print("""
<table border='2'>
<tr>
<th>{}</th>
<th>hi</th>
</tr>
<tr>
<td>bye</td>
<td>bye</td>
</tr>
</table> """.format(x))
