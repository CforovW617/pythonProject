import requests
import re

url='https://weather.com/zh-CN/weather/today/l/CHXX0008:1:CH?Goto=Redirected'
resp=requests.get(url)#打开浏览器并打开网址
#设置一下编码格式
resp.encoding='utf-8'
print(resp.text)#resp响应对象，对象名.属性名 resp.text