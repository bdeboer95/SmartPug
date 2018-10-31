import smtplib
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import settings
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import  COMMASPACE, formatdate

def sendemail( subject, message, files=None):
    #make unit test to check if its a list
    server= smtplib.SMTP('smtp.gmail.com', 587, None, 30)
    server.starttls()
    server.login(settings.login, settings.password)
    msg = MIMEMultipart()
    msg['From'] = settings.login
    msg['To'] = COMMASPACE.join(settings.recipients)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg. attach(MIMEText(message))
    if files:
        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                        fil.read(),
                        Name=basename(f)
                        )# After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)
    problems=server.sendmail(settings.login, settings.recipients, msg.as_string())
    server.quit()
    return problems




