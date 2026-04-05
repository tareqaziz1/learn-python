# Excel

import openpyxl as xl

path = ("./others/transactions.xlsx")
workbook = xl.load_workbook(path)
sheet = workbook["Sheet1"]

for row in range(1, sheet.max_row + 1):
    cell = sheet.cell(row, 2)
    print(cell.value)

# for row in sheet.iter_rows(values_only=True):

sheet.cell(row=1, column=4).value = "Shipping Cost"

for row in range(2, sheet.max_row + 1):
    shipping = 5.5
    shipping_cost = sheet.cell(row, 4).value = shipping
    print(shipping_cost)

for row in sheet.iter_rows(values_only=True):
    print(row)


