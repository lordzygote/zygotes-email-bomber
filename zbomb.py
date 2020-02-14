import os
import smtplib
import getpass
import sys
import time
raw_input = input
print (' *******************************************************************')                                                                   
print (' 8                       welcome to the zygote spammer             8')
print (' 8                         by @lordzygote on ig                    8')
print (' 8                                                                 8')
print (' 8                                                                 8')
print (' 8                                                                 8')
print (' 8                                                                 8')
print (' *******************************************************************')                                                                   

email = input('Attacker Gmail Address : ')
user = input('Anonymous name : ')
passwd = getpass.getpass('Password: ')
to = raw_input('\nTo: ')
body = raw_input('Message: ')
total = input('Number of send: ')
smtp_server = 'smtp.gmail.com'
port = 587

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body  
        server.sendmail(email,to,msg)
        print ("\rE-mails sent: %i") % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print ('\n DONEEEE!!')
except KeyboardInterrupt:
    print ('[-] email Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print ('\n[!] The username or password you entered is incorrect you bafoon.')
    sys.exit()

