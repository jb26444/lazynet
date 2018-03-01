import smtplib       
try:
    content = 'test'

    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo()
    mail.starttls()
    mail.login("jan.blahuta@gmail.com", "xkwnybimmmtlxlxg")
    mail.sendmail("jan.blahuta@gmail.com", "jan.blahuta@updata.net", content)
    mail.quit
    print "Successfully sent email"
except smtplib.SMTPException,error:
    print str(error)
