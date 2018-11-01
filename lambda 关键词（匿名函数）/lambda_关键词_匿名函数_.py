
sum = lambda x,y:x+y
a=input("请输入两个数字：")
a=a.split()
a[0],a[1]=int(a[0]),int(a[1])
sum(a[0],a[1])
print("两数相加的值是：")