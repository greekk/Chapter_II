import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

host = "smtp.mail.ru"
addr_to = "greekks@gmail.com"
addr_from = "sashagrich@mail.ru"
password = 'DerRnX3548'
subj = "Test email from Python"
body = "Python 3.7 rules them all"

msg = MIMEMultipart()
msg['From'] = addr_from
msg['To'] = addr_to
msg['Subject'] = subj
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP_SSL(host, 25)
server.set_debuglevel(True)
#server.starttls()
server.login(addr_from, password)
server.send_message(msg)
server.quit()
