import time
now=time.time()
print(now)

obj=time.localtime()
print(obj)

obj2=time.localtime(60) #60秒
print(obj2)
print(type(obj2))