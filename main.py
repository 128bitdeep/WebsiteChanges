import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import Request, urlopen
import email.utils
from email.mime.text import MIMEText
import config

#paste link of the home page if you want to be notified of all the changes in the site
#paste link of the page if you want to be notified of that particulasr page 
url = Request('www.website.com', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()

while True:
    try:
        currentHash
        #Adjust sleep time as per your requirement
        time.sleep(300)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
        
        if newHash == currentHash:
            continue

        else:
            msg = MIMEText('Change in the website.')
            msg['To'] = email.utils.formataddr(('The Recipient', 'receiver@email.com'))
            msg['From'] = email.utils.formataddr(('Sender Name', 'sender_email@gmail.com'))
            msg['Subject'] = 'Change in Website'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.set_debuglevel(True)
            server.ehlo()
            server.starttls()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            # In order to send email, make necessary changes in the config file
            # Q:Why config file? A: To hide sensitive data on  main script page 
            server.login(f'{config.emailaddr}', f'{config.password}')
            server.sendmail('sender_email@gmail.com', ['receiver@email.com'], msg.as_string())
            server.quit()
            time.sleep(30)
            break

    except Exception as e:
        msg = MIMEText('Change in the website')
        msg['To'] = email.utils.formataddr(('The Recipient', 'receiver@email.com'))
        msg['From'] = email.utils.formataddr(('Sender Name', 'sender_email@gmail.com'))
        msg['Subject'] = 'Change in Website'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(True)
        server.ehlo()
        server.starttls()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(f'{config.emailaddr}', f'{config.password}')
        server.sendmail('sender_email@gmail.com', ['receiver@email.com'], msg.as_string())
        server.quit()
        time.sleep(30)
        #if there is any error, script will skip comparison once and will continue
        continue