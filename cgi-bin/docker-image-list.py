#!/usr/bin/python36

import subprocess as sp

print("Content-type: text/html")
print("\n")

dockerImageList = sp.getoutput("sudo docker images")

dockerimage = dockerImageList.split("\n")






print("""
<html>
<head>
<style>
 .submit-button{
  height:80px;
  width:400px;
  margin-left:35%; 
}
</style>
</head>
<body>
<form action='CAAS-launch.py'>
<table align="center" width='80%' border='1'>
<tr>
<td>Enter ur container name :</td> 
<td><input name='cname' /></td>
</tr>

<tr>
<td>Enter ur image name :</td> 
<td>

<select name='imgname'>

""")


for i in dockerimage[1:] :
	print("<option>")
	j = i.split()
	print(j[0] + ":"  +  j[1])
	print("</option>")


print("""
</select>

</td>
</tr>

<tr>
<td><input type='submit' /></td> 
<td><input type='reset' /></td>
</tr>

</table>
<input class="submit-button" type='button' value='Manage dockers' onclick="window.location.href='http://192.168.43.44/cgi-bin/docker-manage.py'" />
</form>
</body>
</html>
""")


