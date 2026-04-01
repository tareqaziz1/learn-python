# Excel

import openpyxl as xl

path = ("./others/transactions.xlsx")
wordbook = xl.load_workbook(path)
sheet = wordbook["Sheet1"]

for row in range(1, sheet.max_row + 1):
    cell = sheet.cell(row, 1)
    print(cell.value)

for row in sheet.iter_rows(values_only=True):
    print(row)

sheet.cell(row=1, column=4).value = "increased_price" # new header added



