import requests
import logging
import time
#https://stackoverflow.com/questions/14348840/opening-chrome-from-command-line for google commands

logging.basicConfig(filename='Website-Down-Logger',
level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s')

def restart_website():
    from Website_online_tester import Send_Warning_Email
    import os

    command = "sudo gunicorn --bind 0.0.0.0:80 --log-level=debug hello:app"
    os.system("start cmd /c "+command)

    t = (20)
    time.sleep(t)
    try:
        r = requests.get('http://www.spoton.africa/', timeout=5)

        if r.status_code != 200:
            Send_Warning_Email("restart FAILED !!!")
            logging.critical('restart FAILED !!!')
        else:
            logging.info('Website is UP')
            Send_Warning_Email("Website is BACK UP !!")
    except Exception as e:
            logging.critical('restart FAILED !!!')
            Send_Warning_Email("restart FAILED !!!")



restart_website()
