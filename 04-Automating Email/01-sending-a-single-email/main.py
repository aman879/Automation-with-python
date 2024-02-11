import yagmail
import os 
from dotenv import load_dotenv

load_dotenv()

sender = 'aman9693kumar@gmail.com'
receiver = 'dant3kmr@gmail.com'

subject = "This is the subject"

contents = """Here is the content of the email"""

yad = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yad.send(to=receiver, subject=subject, contents=contents)
print("Email sent!")