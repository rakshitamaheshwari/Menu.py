#!/usr/bin/python36

import  cgi
import subprocess as sp
import time
import sys
import atexit

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
cname = form.getvalue('cname')
imgname = form.getvalue('imgname')

#print(cname , imgname)

docker_launch_output = sp.getstatusoutput("sudo ansible-playbook /root/project/docker_caas.yml --extra-vars 'docker_name={c} docker_image={i}'".format(c=cname, i=imgname))

if docker_launch_output[0]  == 0:
#	print("location: docker-manage.py")
	print('Container named {c} LAUNCHED\n'.format(c=cname))
#	print("<a href='docker-manage.py'>click here to manage Container</a>")
else:
	print('Container named {c} failed\n'.format(c=cname))

print("""<p>Redirecting in <span id='countdowntimer'>10 </span> seconds</p>
<script language="javascript" type="text/javascript">
     <!--
     	var timeleft = 10;
	var downloadTimer = setInterval(function(){
	timeleft--;
	document.getElementById("countdowntimer").textContent = timeleft;
	if(timeleft<=0)
		clearInterval(downloadTimer);
	},1000);
	window.setTimeout('window.location="http://192.168.43.44/cgi-bin/docker-manage.py"; ',10000);
     // -->
 </script>
""")
#print("""<script language="javascript" type="text/javascript">
#     <!--
#     window.location="http://192.168.43.182/cgi-bin/docker-manage.py";
#     // -->
# </script>
#""")
#def countdown():
#	for i in range(10,0,-1):
#		sys.stdout.write("\r")
#		sys.stdout.write("Redirecting in {:2d} seconds\n".format(i))
#		sys.stdout.flush()
#		time.sleep(1)
#atexit.register(countdown)


