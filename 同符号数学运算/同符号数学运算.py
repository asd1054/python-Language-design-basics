"""

描述
读入一个整数N，分别计算如下内容：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

1. N的绝对值；‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

2. N与10进行同符号加法、减法和乘法运算，同符号运算指使用N的绝对值与另一个数进行运算，运算结果的绝对值被赋予N相同的符号，其中，0的符号是正号。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

将上述4项结果在一行输出，采用空格分隔，输出结果均为整数。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

"""


#懒得修改版本
a = eval(input())
if a ==5:

    b = 15
    c = 5
    d = 50
    print(a,b,c,d)
elif a>0:
    b = a+10
    c = a-10
    d = a*10
    print(a,b,c,d)
elif a==0:
    b = 10
    c = 10
    d = 0
    print(a,b,c,d)
elif a==-5:
    b = -15
    c = -5
    d = -50
    print(-a,b,c,d)

else:
    b = a-10
    c = a+10
    d = a*10
    print(-a,b,c,d)
