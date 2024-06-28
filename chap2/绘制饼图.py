import pandas as pd
import matplotlib.pyplot as plt
#读取Excel文件
df=pd.read_excel('天气.xlsx',sheet_name='天气')
#print(df)
#解决中文乱码
plt.rcParams['font.sans-serif']=['SimHei']
#设置画布的大小
plt.figure(figsize=(10,6))
labels=df['最高温度']
y=df['最低温度']
# print(labels)
# print(y)

#绘制饼图
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)

#设置x,y轴刻度
plt.axis('equal')
plt.title('各城市天气占比图')
#显示出来
plt.show()

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_set_color.html")
)