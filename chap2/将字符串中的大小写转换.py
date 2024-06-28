def lower_upper(x):
    lst=[]
    for item in x:
        if 'A'<=item<='Z':
            lst.append(chr(ord(item)+32)) #ord(将子没有转换成Unicode码整数，加上32
        elif     'a'<=item<='z':
            lst.append(chr(ord(item)-32))
        else:
            lst.append(item)
    return ''.join(lst)

#准备调用
s=input('请输入一个字符串:')
new_s=lower_upper(s)
print(new_s)
