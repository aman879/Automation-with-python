import pandas as pd
from fpdf import FPDF

df = pd.read_excel('data.xlsx')

for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)

    for col in df.columns[1:]:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=f"{col.title()}:")

        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=row[col], ln=1)

    pdf.output(f"pdf/{row['name']}.pdf")