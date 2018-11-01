

def isPrime(num):
    for i in range(2,num):
        if num%2==0:
            return 0
    return 1

num=int(input())#读入并转换为整数类型

if isPrime(num):#调用isPrime函数判断num是否为素数

    print('yes')

else:

    print('no')