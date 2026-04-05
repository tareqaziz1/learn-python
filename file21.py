# more Excel operations

import openpyxl as xl

path = ("./others/transactions.xlsx")
workbook = xl.load_workbook(path)
sheet = workbook["Sheet1"]

for row in range(1, sheet.max_row + 1):
    cell = sheet.cell(row, 2)
    print(cell.value)


# Add a column as shipping cost

sheet.cell(row = 1, column = 4).value = "shipping_cost"

for row in range(2, sheet.max_row + 1):
    shipping = 5.5
    sheet.cell(row, 4).value = shipping

# Add a column as total cost. total cost will be - price + shipping cost

sheet.cell(row = 1, column = 5).value = "total_cost"

for row in range(2, sheet.max_row + 1):
    cell_price = sheet.cell(row, 3).value
    cell_shipping = sheet.cell(row, 4).value
    total_cost = cell_price + cell_shipping
    total_cost_cell = sheet.cell(row, 5)
    total_cost_cell.value = total_cost
    print(total_cost_cell.value)

# Make a value range based on price. Low (≤10), Medium (11–19), or High (≥20)

sheet.cell(row = 1, column = 6).value = "value_range"

for row in range(2, sheet.max_row + 1):
    price = sheet.cell(row, 3).value
    if price <= 10:
        value = "Low value"
    elif price <= 20:
        value = "Medium value"
    elif price >= 20:
        value = "High value"
    else:
        value = "none"

    sheet.cell(row, 6).value = value

    print(sheet.cell(row, 6).value)

for row in sheet.iter_rows(values_only=True):
    print(row)

#workbook.save('./others/transaction_updated_version2.xlsx')