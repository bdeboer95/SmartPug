import smtplib


subject = 'Babita @ Smart pug'
cc_recipients=[]
msg= 'Hey im sending this to you through the smart pug hihi. How are you?'



def sendemail(sender,recipients, cc_recipients, subject, msg, login,
              password):
    server= smtplib.SMTP('smtp.gmail.com', 587, None, 30)
    server.starttls()
    server.login(emailaddress, password)
    header='From:%s\n' % emailaddress
    header+='To: %s\n' % ','.join(recipients)
    header+='Cc: %s\n'%','.join(cc_recipients)
    header +='Subject:%s\n\n'%subject
    message=header+ msg
    problems=server.sendmail(login, recipients, msg)
    server.quit()
    return problems



