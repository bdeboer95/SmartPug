import smtplib, glob
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


def sendEmail():
    server= smtplib.SMTP('smtp.gmail.com', 587, None, 30)
    server.starttls()
    server.login('smartteddykb81@gmail.com', 'teddy1234!')
    
    motionFile = None
    for file in glob.glob('/home/pi/Desktop/smartteddy/SensorData/Motion/' + "*.txt"):
        motionFile = file
        
    soundFile = None
    for file in glob.glob('/home/pi/Desktop/smartteddy/SensorData/Sound/' + "*.txt"):
        soundFile = file
    
    accelFile = None
    for file in glob.glob('/home/pi/Desktop/smartteddy/SensorData/Accel/' + "*.txt"):
        accelFile = file
        
    msg = MIMEMultipart()
    msg['Subject'] = "see attachments :)" 
    msg['From'] = 'smartteddykb81@gmail.com'
    msg['To'] = 'smartteddykb81@gmail.com'
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(motionFile, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + motionFile)
    msg.attach(part)
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(soundFile, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + soundFile)
    msg.attach(part)
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(accelFile, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + accelFile)
    msg.attach(part)
    
    server.sendmail('smartteddykb81@gmail.com', 'smartteddykb81@gmail.com', msg.as_string())

sendEmail()
