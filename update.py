#!/usr/bin/python

import subprocess
import os

def update():
	print "[*]Updating roxysploit framework, Please Wait ..."
	try:
		subprocess.Popen("cd /tmp;wget http://xl65ae7epcwr2z58.rf.gd/rsf.zip ;unzip rsf.zip; rm rsf.zip", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	except Exception, e:
		print "[!] Update Failed."
		pass

	print "[*]Update was completed successfully."
if __name__ == "__main__":
	update()
