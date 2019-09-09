import smtplib
import requests
import logging
import time

#add code that will rerun the site by opening the terminal and running Gunicorn again.
from Restart_website import restart_website

logging.basicConfig(filename='Website-Down-Logger',
level=logging.WARNING,
format='%(asctime)s:%(levelname)s:%(message)s')


def Send_Warning_Email(message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        EMAIL_ADDRESS = ('edwardtest303@gmail.com')
        EMAIL_PASSWORD = ('Edwardtest101')
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'SPOT ON PAPER > IS DOWN!'
        body = message
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, 'edwardtest303@gmail.com', msg)

def main():
    
    try:
        r = requests.get('http://www.spoton.africa/', timeout=5)

        if r.status_code != 200:
            logging.critical(' Website is DOWN!')
            Send_Warning_Email("Something went wrong. And caused the website go offline.")
            restart_website()
        else:
            logging.info(' Website is UP')
    except Exception as e:
        logging.critical('Website is DOWN!')
        Send_Warning_Email("Something went wrong. And caused the website go offline.")
        restart_website()

while True:
    main()
    #t = (hours*min)*seconds example
    t = (0.30*60)*60
    time.sleep(t)


