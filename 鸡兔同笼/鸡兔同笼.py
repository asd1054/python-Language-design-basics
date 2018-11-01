
#a=input("")
#b=a.split(' ')
#b[0]=int(b[0])
#b[1]=int(b[1])
#def work(a,b):
#    for i in range(101):
#        for j in range(101):
#           if (2*i+4*j==b[1] and i+j==b[0]):
#               return i,j
#c=work(a,b)
#print(c[0],c[1])

#刘美馨
#print("请输入头和脚的数量: ")
a=input("")
b=a.split(' ')
head=int(b[0])
foot=int(b[1])
#x=0#兔子的个数
y=0#鸡的个数
#head,foot=eval(input(""))
for i in range(1,foot//4):
    y=head-i
    if 4*i+2*y==foot:
        #print("兔子有%d,鸡有%d"(i,y))
        print(i,y)
        break