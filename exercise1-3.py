# Compute an approximation to pi using Monte Carlo. Use no imports besides
#
# Consider the circle of diameter 1 embedded in the unit square
# Let  A  be its area and let  r=1/2  be its radius


import numpy as np

n = 1000000

count = 0
for i in range(n):
    u, v = np.random.uniform(), np.random.uniform()
    d = np.sqrt((u - 0.5)**2 + (v - 0.5)**2)
    if d < 0.5:
        count += 1

area_estimate = count / n
p = area_estimate * 4

print('π = ' + str(p))
