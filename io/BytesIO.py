# coding:utf-8

from io import BytesIO

# write to BytesIO
f = BytesIO()
f.write(b'hello')
f.write(b'\n')
f.write(b'python')
print(f.getvalue())

f = BytesIO('welcome to python'.encode('utf-8'))
print(f.read())
