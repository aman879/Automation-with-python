import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender = "automatepython084@outlook.com"
receiver = "dant3kmr@gmail.com"
password = os.getenv("OPASSWORD")

subject = "Hello Hello"
body = "This is Me! Just want to say hi!"

# Combine subject and body with two newline characters
message = f"Subject: {subject}\n\n{body}"

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()