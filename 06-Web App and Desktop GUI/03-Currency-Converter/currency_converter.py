from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currecny):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currecny}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[0:-4])
    return rate


def convert():
    input_text = text.text()
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentText()
    input_text = float(input_text) * get_currency(in_cur, target_cur)
    
    output_label.setText(str(input_text) + " " + target_cur)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency converter')

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)


in_combo = QComboBox()
currencies = ['USD', 'EUR', 'INR']
in_combo.addItems(currencies)
layout1.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout1.addWidget(target_combo)

layout2 = QHBoxLayout()
layout.addLayout(layout2)

text = QLineEdit()
layout2.addWidget(text)

btn = QPushButton('Convert')
layout2.addWidget(btn)
btn.clicked.connect(convert)


output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()