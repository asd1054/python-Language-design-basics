
for i in range (2,1000):
    for j in range(2,i//2):
        
        if (i%j==0):
            break
    else:
        #for也可以和else搭配出现，在这段代码里，当某一次遍历结果余数为0后，break生效，那循环就结束了，那与之成对出现的else代码也就不执行了；当所有遍历结束后没有一次余数为0，那该循环就转到else开始执行，打印输出“该数为质数”。
        print(i)

#判断是否为素数
a = int(input("请输入一个数："))
pd = 1
for j in range(2,a//2):
    if (a%j==0):
        print(a,"不是素数")
        pd = 0
        break

if pd ==1:
    print(a,"是素数")