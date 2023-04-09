from configparser import ConfigParser
import os
from pathlib import Path
from email.message import EmailMessage
import ssl
import smtplib 
from _UI_DESIGNS.UI import *
import base64


file = 'config.ini'
config = ConfigParser()
config.read(file)

def update_Sender(email,passw):
    email = b64_encode_decode(email,True)
    passw = b64_encode_decode(passw,True)
    try:
        config['SENDER'] = {
            'email': email,
            'password':passw
            }
    
        with open(file,'w') as configfile: # 'w' stands for write mode
            config.write(configfile)
    
    except:
        print("THERE WAS AN ERROR UPDATING CONFIGURATION")
    
    email = b64_encode_decode(email,False)
    passw = b64_encode_decode(passw,False)
    print(email,passw)
    
def update_Receiver(email,subject,message):
    email = b64_encode_decode(email,True)
    subject = b64_encode_decode(subject,True)
    message = b64_encode_decode(message,True)

    try:
        config['RECEIVER'] = {
            'email': email,
            'subject':subject,
            'message':message
            }       
        with open(file,'w') as configfile: # 'w' stands for write mode
            config.write(configfile)
    
    except:
        print("THERE WAS AN ERROR UPDATING CONFIGURATION FILE")
    


def file_check(file):
    if not os.path.isfile(file):
        file = Path('config.ini')
        file.touch(exist_ok=True)
        config.add_section('SENDER')
        config.set('SENDER','email','')
        config.set('SENDER','password','')
        config.add_section('RECEIVER')
        config.set('RECEIVER','email','')
        config.set('RECEIVER','subject','')
        config.set('RECEIVER','message','')
        with open(file, 'w') as configfile:
                config.write(configfile)







def send(email_receiver,subject,message,email_sender,email_password):
    email_sender =email_sender
    # email_password = os.environ.get('EMAIL_PASSWORD')
    email_password = email_password
    email_receiver = email_receiver


    subject = subject
    body =message

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    

    print("WHAT I HAVE",email_receiver,subject,body,email_sender,email_password)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
            print("sent")

    except Exception as e:
        print(e)
        return False

    

#if true it will encode,decode if not
def b64_encode_decode(input_string, encode_me):
        b = input_string.encode('UTF-8')
        e = base64.b64encode(b) if encode_me else base64.b64decode(b)
        return e.decode('UTF-8')



# file_check(file)
# update_Sender("Email","Password")