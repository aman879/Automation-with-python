import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

sender = "automatepython084@outlook.com"
receiver = "dant3kmr@gmail.com"
password = os.getenv("OPASSWORD")

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again'

body = """
<h2>Hii there!</h2>
What my man doin'
"""

mimmetext = MIMEText(body, 'html')
message.attach(mimmetext)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()