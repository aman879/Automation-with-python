import gspread
import re

gc = gspread.service_account('secret.json')

spreadsheet = gc.open("Automation_spreadSheet_private")

# Get a worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0)

# Get a worksheet by name
worksheet1 = spreadsheet.worksheet('2013')

data = worksheet1.get_all_records()

# Get Rows

data_row = worksheet1.get_values('A5:E5')

# get a row by index
data_row_i = worksheet1.row_values(3)

# Get a Column by index
data_col = worksheet1.col_values(2)[1:]

# Get a row by cell
data_row_cell = worksheet1.get_values('D5')[0][0]

# Get cell using cell
data_cell = worksheet1.acell('D5').value

# Search for a cell
cell = worksheet1.find('-10')
# print(cell.row, cell.col)

# Search for many cells
cells = worksheet1.findall('-9')

# for cell in cells:
#     print(cell.row, cell.col)

# search with regural expression

reg = re.compile(r'99')
rCells = worksheet1.findall(reg)

# for cell in rCells:
#     print(cell.row, cell.col)

# Update a cell
worksheet1.update_cell(5, 5, -39)

# update a