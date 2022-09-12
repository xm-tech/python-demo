#coding:utf-8
from datetime import datetime

## open 这种写法，可以不用再关闭文件
with open('text.txt', 'a') as f:
    f.write('today is :')
    f.write(datetime.now().strftime('%Y-%m-%d') + '\n')

## 读utf8文本文件
with open('text.txt', 'r') as f:
    # 读取整块文件
    # print(f.read())

    for line in f.readlines():
        print(line.strip())  # 去掉末尾的 '\n'

## 读取指定编码文件
# with open('text.txt', 'r', encoding='gbk') as f:
#     print(f.read())
