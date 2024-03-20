import pandas as pd

url_sheet1 = "https://docs.google.com/spreadsheets/d/1P3qhB6HjY_IoKCwxTpRWyVhb3ZWK7Ydz_TjATJp0EG0/gviz/tq?tqx=out:csv&sheet=2013"
url_sheet2 = "https://docs.google.com/spreadsheets/d/1P3qhB6HjY_IoKCwxTpRWyVhb3ZWK7Ydz_TjATJp0EG0/gviz/tq?tqx=out:csv&sheet=2014"
data1 = pd.read_csv(url_sheet1)
data2 = pd.read_csv(url_sheet2)

print(data1)
print(data2)