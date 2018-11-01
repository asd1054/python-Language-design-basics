'''
描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。请问该青蛙跳上一个n级的台阶总共有多少种跳法。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

输入台阶数，输出一共有多少种跳法‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

注意：如果运算超时，请思考有什么办法降低时间复杂度。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
'''
from scipy.special import comb, perm
#comb 组合
#perm 排列
from math import *

#oj不支持组合，于是自己写一个
#def comb(sum,num):


def work(num):
    sum=1
    #计算出最多有几个二
    if num>1:
        c=int(ceil(num/2)) #奇数+1
        c1=int(floor(num/2))    #整数 偶数
        even = 0
        if c==c1:
            even = 1

        while 1:
            
            for i in list(range(c1,0,-1)):
                if even:
                    sum += comb(c1,i)

                else:
                    sum+=comb(c1+1,i)

                c1+=1
            
            
            return sum

    else:
        return sum

num = int(input())
sum =int(work(num))
print(sum)


        
        