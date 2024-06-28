import jieba
#读取文件
with open('weiwei.txt', 'r', encoding='ANSI') as file:
    s=file.read()
# print(s)
#分词
lst = jieba.lcut(s)
print(lst)
