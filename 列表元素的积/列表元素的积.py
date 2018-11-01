'''
描述

一个由n(n>1)个数字组成的列表 ls，输出一个列表lt，其中lt中第i个元素等于ls中除ls[i]之外所有元素的乘积
'''

from _functools import reduce

def work(num,n):
    l = len(num)
    sum = 1
    for i in range(l):
        if i==n:
            continue
        sum *=int(num[i])
    return sum

ls = input()
ls = ls[1:-1]
ls = ls.split(',')
lt = []
l = len(ls)
for i in range(l):

    #lt.append(int(work(ls,i)/int(ls[i])))
    lt.append(int(work(ls,i)))
print(lt)