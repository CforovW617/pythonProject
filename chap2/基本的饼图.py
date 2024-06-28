#导入
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
#准备数据
lst=[['华为',1000],['oppo',1200],['苹果',300],['小米',1300]]
c = (
    Pie()
    .add("", lst)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="2024年手机销量占比情况"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_set_color.html")
)