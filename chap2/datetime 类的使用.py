from datetime import datetime #从datetime模块中 导入datetime类
dt=datetime.now()
print('当前的系统时间为：',dt)

#datetime是一个类，手动创建这个类
dt2=datetime(2024,6,25,5,20)
print('dt2的数据类型',type(dt2),'dt2所表示的日期时间:',dt2)
print('年:',dt2.year,'月：',dt2.month,'日:',dt2.day)
print('时:',dt2.hour,'分:',dt2.minute,'秒:',dt2.second)

#比较两个datetime类型对象的大小
labor_day=datetime(2028,5,1,0,0,0)
national_day=datetime(2028,10,1,0,0,0)
print('2028年5月1日比2028年10月1日早吗？',labor_day<national_day)