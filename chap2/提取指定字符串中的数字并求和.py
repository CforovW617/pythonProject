
def get_digit(x):
    s=0
    lst=[]
    for item in x:
        if item.isdigit():
            lst.append(int(item))

    s=sum(lst)
    return lst,s


s=input('请输入一个字符串:')
#调用
lst,x=get_digit(s)
print('提取的数字列表为:',lst)
print('累加和为:',x)