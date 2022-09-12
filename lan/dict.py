#coding:utf-8
## dict,map

import time

d = {"maxm": 1985, "wxl": 2008}
print(d['maxm'], d['wxl'], d.get('lfj', 'nil'))
d.pop('maxm')
print(d.get('maxm'))

## list
name_list = ['maxm', 'maxm', 'wxl']
print('name_list:', name_list)
for n in name_list:
    print(n)
print('----')

## set
age_set = set([37, 37, 14])
age_set.add(37)
print('ages:')
for a in age_set:
    print(a)
age_set.remove(14)
for a in age_set:
    print(a)
print('----')
## for loop
sum = 0
for x in range(10):
    sum += x
print(sum)

sum = 0
for x in range(8, 10):
    sum += x
print(sum)


## func
def Sum(a, b):
    return a + b


print(Sum(3, 5))


## x ^ n, 不传参数 n 时，n 默认为2
def power(x, n=2):
    ret = 1
    while (n > 0):
        n -= 1
        ret = ret * x
    return ret


print(power(2, 10))
print(power(5))

## time elapsed
t0 = time.time()
time.sleep(0.5)
t1 = time.time()
# 保留小数点后2位
print("Took {:.2f} seconds".format(t1 - t0))
print("t0:{:.2f}".format(t0))


## closure
def run():
    num = 0

    def incr(amount):
        return num + amount

    num = incr(1)
    num = incr(2)
    print(num)


run()
