from random import random
from math import sqrt
from time import clock
DARTS = 10000
hits =0.0
clock()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = sqrt(x**2+y**2)
    if dist<=1.0:
        hits +=1
pi = 4*(hits/DARTS)
print("pi的值是{}".format(pi))
print("运行的时间是{:5.5}s".format(clock()))