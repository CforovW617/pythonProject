# encoding=utf-8
import  pdfplumber
# 打开pdf文件
with pdfplumber.open('C:\\Users\\lyw\\Desktop\\考编\\三级信息安全技术考试大纲.pdf')as pdf:
    for i in pdf.pages:#遍历页
        print(i.extract_text()) #extract_text方法提取内容
        print(f'------------第{i.page_number}页结束')
