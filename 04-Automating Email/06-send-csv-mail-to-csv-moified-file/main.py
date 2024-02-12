import yagmail
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

sender = 'aman9693kumar@gmail.com'

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pd.read_csv('contacts.csv')

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))

for index, row in df.iterrows():
    name = row['name']
    filename = name + ".txt"
    amount = row['amount']
    generate_file(filename, amount)

    receiver_email = row['email']
    subject = f"{name} bill"
    content= [f"""
              Hey, {name} you have to pay {amount}
            Bill is attached""",
            filename]
    yag.send(to=receiver_email, subject=subject, contents=content)
    print("Email send to", name)

