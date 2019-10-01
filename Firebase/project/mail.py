import smtplib

toaddrs= 'ajayyasodha@gmail.com'
fromaddr  = 'haniel20008@gmail.com'
SUBJECT="Mark ME!- Automated mail generation"
TEXT="Please ensure that you have missed your classes today.\n STUDENT ID: Ajay Kumar \n COURSE: BE "
msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

username = 'haniel20008@gmail.com'
password = '9677051833 '

server = smtplib.SMTP('smtp.gmail.com','587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()