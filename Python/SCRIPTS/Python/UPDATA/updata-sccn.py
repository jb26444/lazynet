#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import email.utils
import smtplib
import sys
import paramiko
import time
import getpass
import os
from host_seedfile import network_devices
from host_config_file import host_conf
from host_config_file import host_conf_1

 
UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")
FN = raw_input("File-name Pre : ")
FN_1 = raw_input("File-name Work : ")

def email():
  recipients = ['jan.blahuta@updata.net',] 
  emaillist = [elem.strip().split(',') for elem in recipients]
  msg = MIMEMultipart()
  msg['Subject'] = "Pre-COMMS UPDATA SCCNXXX TEST1"
  #msg['From'] = 'jan.blahuta@updata.net'
  msg['Reply-to'] = 'jan.blahuat@updata.net'
 
  msg.preamble = 'Multipart massage.\n'
 
  part = MIMEText("This is Pre-COMMS email with attached file for Pre-COMMS Health Cheks")
  msg.attach(part)
 
  part = MIMEApplication(open(FN,"rb").read())
  part.add_header('Content-Disposition', 'attachment', filename=FN)
  msg.attach(part)
 

  server = smtplib.SMTP("mail.updata.net", 587)
  server.ehlo()
  server.starttls()
  server.login("jan.blahuta", "Password16")
 
  server.sendmail(msg['From'], emaillist , msg.as_string())

def postemail():
  recipients = ['jan.blahuta@updata.net',] 
  emaillist = [elem.strip().split(',') for elem in recipients]
  msg = MIMEMultipart()
  msg['Subject'] = "Post-COMMS UPDATA SCCNXXX TEST1"
  #msg['From'] = 'automation@secorg.net'
  msg['Reply-to'] = 'jan.blahuat@updata.net'
 
  msg.preamble = 'Multipart massage.\n'
 
  part = MIMEText("This is Post-COMMS email with attached file for Post-COMMS Health Checks and work carried on each device")
  msg.attach(part)
 
  part = MIMEApplication(open(FN_1,"rb").read())
  part.add_header('Content-Disposition', 'attachment', filename=FN_1)
  msg.attach(part)
 

  server = smtplib.SMTP("mail.updata.net", 587)
  server.ehlo()
  server.starttls()
  server.login("jan.blahuta", "Password14")
 
  server.sendmail(msg['From'], emaillist , msg.as_string())

if __name__ == '__main__':

 for ip in  network_devices:
    print ip
    twrssh = paramiko.SSHClient()
    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    twrssh.connect(ip, port=22, username=UN, password=PW)
    remote = twrssh.invoke_shell()
    remote.send('term len 0\n')
    time.sleep(1)
    #This for loop uses config file 'host_config1.py' to enter commands one by one
    for command in host_conf:
        remote.send(' %s \n' % command)
        time.sleep(2)
        buf = remote.recv(65000)
        print buf
        f = open(FN, 'a')
        f.write(buf)
        f.close()
    twrssh.close()
 print ("Pre-COMMS EMAIL")
 email()
 for ip in  network_devices:
    print ip
    twrssh = paramiko.SSHClient()
    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    twrssh.connect(ip, port=22, username=UN, password=PW)
    remote = twrssh.invoke_shell()
    remote.send('term len 0\n')
    time.sleep(1)
    #This for loop uses config file 'host_config1.py' to enter commands one by one
    for command in host_conf_1:
        remote.send(' %s \n' % command)
        time.sleep(2)
        buf = remote.recv(65000)
        print buf
        f = open(FN_1, 'a')
        f.write(buf)
        f.close()
    twrssh.close()
 for ip in  network_devices:
    print ip
    twrssh = paramiko.SSHClient()
    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    twrssh.connect(ip, port=22, username=UN, password=PW)
    remote = twrssh.invoke_shell()
    remote.send('term len 0\n')
    time.sleep(1)
    #This for loop uses config file 'host_config1.py' to enter commands one by one
    for command in host_conf:
        remote.send(' %s \n' % command)
        time.sleep(2)
        buf = remote.recv(65000)
        print buf
        f = open(FN_1, 'a')
        f.write(buf)
        f.close()
    twrssh.close()
    print ("Post-COMMS EMAIL")
 
postemail()

print ("script completed")







 







