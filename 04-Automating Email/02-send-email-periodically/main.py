import yagmail
import os
from dotenv import load_dotenv
import time

load_dotenv()

sender = 'aman9693kumar@gmail.com'
receiver = 'datn3kmr@gmail.com'

subject = """Some subject"""

contents = """content"""

i=1
while i <= 5:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    content = contents + " " + str(i)
    yag.send(to=receiver, subject=subject, contents=content) 
    print("Email sent")
    i+=1
    time.sleep(15)
    