import smtplib

def sendemail(sender,recipients, cc_recipients, subject, msg, login,
              password):
    server= smtplib.SMTP('smtp.gmail.com', 587, None, 30)
    server.starttls()
    server.login(login, password)
    header='From:%s\n' % login
    header+='To: %s\n' % ','.join(recipients)
    header+='Cc: %s\n'%','.join(cc_recipients)
    header +='Subject:%s\n\n' %subject
    message=header+ msg
    problems=server.sendmail(login, recipients, message)
    server.quit()
    return problems



