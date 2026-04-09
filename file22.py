# Charts with openpyxl

import openpyxl as xl
from openpyxl.chart import BarChart, LineChart, PieChart, Reference

path = "./others/transactions_updated_v2.xlsx"
workbook = xl.load_workbook(path)
sheet = workbook["Sheet1"]

bar_chart = BarChart()  # Making a bar chart

data = Reference(sheet, min_col=3, min_row=1, max_row=sheet.max_row)
category = Reference(sheet, min_col=2, min_row=2, max_row=sheet.max_row)

bar_chart.add_data(data, titles_from_data=True)
bar_chart.set_categories(category)
bar_chart.title = "Price per product"
sheet.add_chart(bar_chart, "A25")


pie = PieChart()        # Making a pie chart

data = Reference(sheet, min_col=6, min_row=1, max_row=3)
labels = Reference(sheet, min_col=8, min_row=2, max_row=3)






#workbook.save("./others/transactions_updated_v3.xlsx")