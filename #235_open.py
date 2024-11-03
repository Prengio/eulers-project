from func import polyeval, newt_raph, time
import numpy as np

poly = [600000000897]

for i in range(2, 5001):
    poly.append((900-3*i))

print(len(poly))

roots = np.roots(poly)

for i in roots:
    if i.imag == 0:
        print(i)
time()