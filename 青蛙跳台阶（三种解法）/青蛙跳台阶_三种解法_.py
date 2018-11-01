

class Solution:
    # @param {integer} n
    # @return {integer}

    #递归
    def recursion(self, n):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.recursion(n-1)+self.recursion(n-2)

    #循环 模拟递归
    def circulation(self, n):
        if n==1 or n==2:
            return n
        a=1;b=2;c=3
        for i in range(3,n+1):
            c=a+b;a=b;b=c
        return c

    #建立简单数学模型，利用组合数公式
    def comb(self, n):
        def fact(n):#数的阶乘
            result=1
            for i in range(1,n+1):
                result*=i
            return result
        total=0
        for i in range(n/2+1):
            total+=fact(i+n-2*i)/fact(i)/fact(n-2*i)
        return total
num = int(input())
solve = Solution()
sum = solve.recursion(num)#递归
print(sum)