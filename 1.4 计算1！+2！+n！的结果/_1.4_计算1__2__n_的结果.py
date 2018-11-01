
sum=0
temp=1
n=input("请输入一个整数：")
n=int(n)
for i in range(1,n+1):
    temp*=i
    sum+=temp
print(sum)