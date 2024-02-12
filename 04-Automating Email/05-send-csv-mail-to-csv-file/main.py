import yagmail
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

sender = 'aman9693kumar@gmail.com'

subject = "Your bill"

df = pd.read_csv('contacts.csv')

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

for index, row in df.iterrows():
    contents = [f"""Hey {row['name']} you have to pay {row['amount']}""", """Bill is attached""", row['filepath']]
    yag.send(to=row['email'], subject=subject, contents=contents)
    print('Email sent')