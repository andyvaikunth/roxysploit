#!/usr/bin/python

import os
import urllib, urllib2
import sys
import time
import socket
import whois
import logging
from subprocess import check_output

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

subdomains = ["ftp", "cpanel", "webmail", "forum", "driect-connect", "vb", "forums", "home", "direct", "mail", "access", "admin", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5"]

def main():
 if len(sys.argv) == 2:
    url = sys.argv[1]
    print "\033[1;94m[?]\033[1;m Getting reverse dns\033[1;m"
    reversed_dns = urllib.urlopen('http://api.hackertarget.com/reverseiplookup/?q=' + url).read()
    print "\033[1;94m[?]\033[1;m Getting geoip\033[1;m"
    geoip = urllib.urlopen('http://api.hackertarget.com/geoip/?q=' + url).read()
    print "\033[1;94m[?]\033[1;m Scanning ports\033[1;m"
    nmap = check_output("nmap -A -sS " + url + "", shell=True)
    print "\033[1;94m[?]\033[1;m Getting httpheaders\033[1;m"
    httpheaders = urllib.urlopen('http://api.hackertarget.com/httpheaders/?q=' + url).read()
    print "\033[1;94m[?]\033[1;m Getting tracert\033[1;m"
    tracert = urllib.urlopen('http://api.hackertarget.com/mtr/?q=' + url).read()
    print "\033[1;92m[*]\033[1;m Reverse dns information:"
    print reversed_dns
    print "\033[1;92m[*]\033[1;m Geoip information:\033[1;m"
    print geoip
    print "\033[1;92m[*]\033[1;m Port scan information:\033[1;m"
    print nmap
    print "\033[1;92m[*]\033[1;m httpheader information:\033[1;m"
    print httpheaders
    print "\033[1;92m[*]\033[1;m tracert information:\033[1;m"
    print tracert
    time.sleep(0.7)
    print "\033[1;92m[*]\033[1;m Starting cloudflare resolver\033[1;m"
    time.sleep(2)
    print "\033[1;92m[*]\033[1;m Starting website reconnaissance\033[1;m"
    os.system('sh ' + RescoursesDir + '/plugins/extractor.sh ' + url + '')
 else:
    print ""

def cf():
    link = sys.argv[1]
    for sbdm in subdomains:
      try:
         hosts = str(sbdm) + "." + str(link)
         trueip = socket.gethostbyname(str(hosts))
         print "[!] Discovered >> " + str(trueip)
      except:
             pass

main()
cf()
