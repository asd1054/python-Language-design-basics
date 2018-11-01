
# 例如153、370、371及407就是三位超完全数字不变数，其各个数之立方和等于该数：

d=[]
for i in range (100,1000):
    a=i//100
    b=i//10%10
    c=i%10
    if(i==a**3+b**3+c**3):
        #print(i)
        d.append(i)

l = len(d)
for i in range(l):
    if i!=l-1:
        print("%d, "%d[i],end='')
    else:
        print("%d"%d[i])


print("153, 370, 371, 407")