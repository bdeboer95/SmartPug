import smtplib, glob, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


def sendEmail():
    server= smtplib.SMTP('smtp.gmail.com', 587, None, 30)
    server.starttls()
    server.login('smartteddykb81@gmail.com', 'teddy1234!')
    
    motionFile = None
    files = glob.glob('/home/pi/Desktop/smartteddy/SensorData/Motion/' + "*.txt")
    files.sort(key=os.path.getmtime)
    for file in files:
        motionFile = file
    
    soundFile = None
    files = glob.glob('/home/pi/Desktop/smartteddy/SensorData/Sound/' + "*.txt")
    files.sort(key=os.path.getmtime)
    for file in files:
        soundFile = file
    
    accelFile = None
    files = glob.glob('/home/pi/Desktop/smartteddy/SensorData/Accel/' + "*.txt")
    files.sort(key=os.path.getmtime)
    for file in files:
        accelFile = file
        
    msg = MIMEMultipart()
    msg['Subject'] = "see attachments :)" 
    msg['From'] = 'smartteddykb81@gmail.com'
    msg['To'] = 'smartteddykb81@gmail.com'

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(motionFile, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + os.path.basename(motionFile))
    msg.attach(part)
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(soundFile, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + os.path.basename(soundFile))
    msg.attach(part)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(accelFile, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + os.path.basename(accelFile))
    msg.attach(part)
    
    server.sendmail('smartteddykb81@gmail.com', 'smartteddykb81@gmail.com', msg.as_string())

sendEmail()
