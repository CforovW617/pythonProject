import my_info
print(my_info.name)
my_info.info()

import my_info as a
print(a.name)
a.info()

#(2)from..inport
from my_info import name
print(name)

from my_info import info
info()

#通配符
from my_info import *

print(name)
info()

#同时导入多个模块
import math,time,random
