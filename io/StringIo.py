# coding:utf-8

# 从 io 包导入 StringIO 这个类
from io import StringIO

# write to StringIO
f = StringIO()
f.write('hello ')
f.write('python')

print(f.getvalue())
