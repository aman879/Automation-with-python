from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('logo.jpeg', w=140, h=140)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=35, txt="My Data", align='C', border=1, ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=25, txt="Description", ln=1)

pdf.set_font(family='Times', size=12)
txt1 = """Data usage is how much data your phone uploads or downloads using mobile data.
To make sure that you're not using too much data on your data plan, you can check and change your data usage.

Important: You're using a custom Android version. If these steps don't work for you, check with your device manufacturer.Important: Some of these steps work only on Android 8.0 and up. Learn how to check your Android version."""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt="Name")

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Aman Kumar', ln=1)

pdf.output('output.pdf')