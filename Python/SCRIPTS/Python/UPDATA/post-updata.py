#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import email.utils
import smtplib
import sys


recipients = ['jan.blahuta@updata.net',] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "SCCN TEST"
#msg['Subject'] = str(sys.argv[1])
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
