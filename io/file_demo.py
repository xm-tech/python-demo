# coding: utf-8

import os

# data = input("plz input: ")
# print(data)

# 获取当前路径的绝对路径
print(os.path.abspath('.'))
path = '/Users/maxiongmiao/python/net'

if (os.path.exists(path)):
    print(path, ' already exsits')
else:
    os.mkdir(path)

if (os.path.exists(path)):
    os.rmdir(path)
    print(path, ' removed')
