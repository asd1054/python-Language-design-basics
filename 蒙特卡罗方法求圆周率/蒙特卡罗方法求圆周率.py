import random
n=1000000#一百万
k=0
for i in range(n):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if y<x**2:
        k=k+1

print ("PI："，float(k)/float(n))
