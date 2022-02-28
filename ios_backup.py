import sys
import time
import paramiko
import os
import cmd
import datetime


now = datetime.datetime.now()


USER = 'wwwprcdn03'
PASSWORD = 'Wwwprcdn03'
secret = 'tpslab03!'

f = open('cisco_hosts')
for ip in f.readlines():
	ip = ip.strip()
	filename_prefix ='cisco_backup' + ip


	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=USER, password=PASSWORD)

	chan = client.invoke_shell()
	time.sleep(2)

	chan.send('en\n')
	chan.send(secret +'\n')
	time.sleep(1)
	chan.send('term len 0\n')
	time.sleep(1)
	chan.send('sh run\n')
	time.sleep(10)
	output = chan.recv(99999)
	print output
	filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
	ff = open(filename, 'a')
	ff.write(output)
	ff.close()
	client.close()

	print ip
	f.close()
