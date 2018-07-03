import smtplib
from app import app


def sendmail(name, email, phone, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('SOMEONE@gmail.com','PASSWORD')
    MESSAGE = '''
    From: {}
    Email: {}
    Phone: {}
    Subject: Blog Contact Me Form.

    {}
    '''.format(name, email, phone, message)
    server.sendmail('SOMEONE@gmail.com','SOMEONEELSE@gmail.com',MESSAGE)
    server.quit()

