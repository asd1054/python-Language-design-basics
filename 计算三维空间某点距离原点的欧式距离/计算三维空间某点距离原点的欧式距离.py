from math import sqrt

def distance(x,y,z):
    dist = sqrt(x*x+y*y+z*z)
    return dist
    
num = input()

x,y,z = num.split(',')
# num= num.split(',')
# ‪‬‮‬‪‬‪‬x=num[0]
# y=num[1]
# z=num[2]
d=distance(float(x),float(y),float(z))#调用distance函数‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

print("{:.2f}".format(d))#输出距离值，保留三维小数‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬ 
