import weather
import openpyxl
html=weather.get_html()#发请求，得响应结果
lst=weather.parse_html(html)#解析数据
#创建一个新得excel工作簿
workbook=openpyxl.Workbook() #创建对象
#在excel文件中创建工作表
sheet=workbook.create_sheet('天气')
#像工作表中添加数据
for item in lst:
    sheet.append(item)#一次添加一行

workbook.save('天气.xlsx')