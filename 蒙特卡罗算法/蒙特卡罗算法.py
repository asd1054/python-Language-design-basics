
import random
import numpy as np
import math

N = 10000
sum = 0
for i in range(N):
        rg = random.gauss(0,1)
        if rg > 1 or rg < -1:
                continue
        sum += np.exp(rg + 0.5 * (rg**2))

sum *= math.sqrt(2 * math.pi)
sum /= N

print(sum)