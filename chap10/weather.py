import requests
import re

#定义函数
def get_html():
    url = 'http://www.nmc.cn/publish/forecast.html'
    resp=requests.get(url)
    #设置一下编码格式
    resp.encoding='utf-8'
    return (resp.text)
def parse_html(html_str):
    city=re.findall('class=city><div class=row><div class=col-xs-3> ([\u4e00-\u9fa5]*) </div><div class="col-xs-3 wdesc">', html_str)
    weather=re.findall('class="col-xs-3 wdesc"> ([\u4e00-\u9fa5]*) </div>', html_str)
    hight_tem=re.findall('<span class=hight>([\d]*℃)</span>', html_str)
    low_tem=re.findall('<span class=low>([\d]*℃)</span>', html_str)
# print(city)
# print(weather)
# print(hight_tem)
# print(low_tem)

    lst=[]
    for a,b,c,d in zip(city,weather,hight_tem,low_tem):
        lst.append([a,b,c,d])
    print(lst)
    for item in lst:
        print(item)
    return lst