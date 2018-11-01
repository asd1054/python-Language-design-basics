
a=99
b=98
c=97
d=96
e=95
ave=0
def average():
    ave=(a+b+c+d+e)/5
    print("平均值：",ave)

def variance():#方差
    sum =0 
    #average()
    ave=(a+b+c+d+e)/5
    for i in [a,b,c,d,e]:
        sum+=(i-ave)**2
    sum/=5
    print("方差：",sum)

def median():
    f=[a,b,c,d,e]
    for i in range(4):
        if (f[i]>f[i+1]):
            t=f[i]
            f[i]=f[i+1]
            f[i+1]=t
    print("中位数：",f[3])
average()

variance()

median()
