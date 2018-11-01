print("用户输入一个正整数N，计算从1到N相加之后的结果")
n=input("请输入整数N：")#n为字符串类型
sum=0
n=int(n)+1
for i in range(n):
    sum+=i
print("最后结果为：%d"%sum)

