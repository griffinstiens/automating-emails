# Simple mail transfer protocol
import smtplib
# email module that comes built in with Python
from email.message import EmailMessage
from dotenv import load_dotenv
from decouple import config
import sys

CLIENT_PASSWORD = config('PASS')
CLIENT_EMAIL = config('EMAIL')

load_dotenv()

email = EmailMessage()
email['from'] = 'Griffin Stiens'
# Who the email is going to - Don't need to enable "less secure apps" on this account
email['to'] = 'griffinstiens@gmail.com'
email['subject'] = 'tHiS iSnT sPaM'

email.set_content('You got jebaited')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # hello message
    smtp.ehlo()
    # Encryption method to connect to server
    smtp.starttls()
    # This is where you have to enable less secure apps in order for this to work
    smtp.login(CLIENT_EMAIL, CLIENT_PASSWORD)
    smtp.send_message(email)
    print('Email has been successfully sent)










