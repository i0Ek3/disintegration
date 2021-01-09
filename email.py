#!/usr/bin/env python
# coding=utf-8

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

# TODO: make this script available
def email(sender, receivers, passwd):
    # create a email message object with attachment
    msg = MIMEMultipart()

    # txt content 
    content = MIMEText('this is a test email', 'plain', 'utf-8')
    msg['Subject'] = Header('Data', 'utf-8')
    msg.attach(content)

    # read file and add it as attachment into email message object
    with open('./pytest/test.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/palin'
        txt['Content-Disposition'] = 'attachment; filename=test.txt'
        msg.attach(txt)

    # create SMTP object
    # ref: https://www.bitrecover.com/imap-settings/q-email/
    smtper = smtplib.SMTP('smtp.qq.com', 587)
    smtper.starttls()
    smpter.login(sender, passwd)
    smtper.sendmail(sender, receivers, msg.as_string())
    smtper.quit()
    print("email already sent!")
