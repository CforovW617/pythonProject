import openpyxl
#打开工作簿
workbook=openpyxl.load_workbook('天气.xlsx')
#选择要操作得工作表
sheet=workbook['天气']
#表格数据是二维列表，先遍历的是行，后遍历的是列
lst=[]#存储的是行数据
for row in sheet.rows:
    sublst=[]#存储单元格数据
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)

for item in lst:
    print(item)