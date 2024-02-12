import yagmail
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

sender = 'aman9693kumar@gmail.com'
receiver = 'dant3kmr@gmail.com'

subject="""Some subject"""

contents = ["""Some content""", 'logo.pdf']

att = Path('logo.pdf')

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print('Email sent')
