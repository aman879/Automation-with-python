import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

sender = 'automatepython084@outlook.com'
receiver = 'dant3kmr@gmail.com'
password = os.getenv('OPASSWORD') 

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Some subject'

body = """
<h1>Hello</h1>
How are you my friend?
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)

attachment_path = 'logo.pdf'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachement', filename=attachment_path)
message.attach(payload)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()