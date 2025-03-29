from math import gcd
from func import time
import sys

sys.set_int_max_str_digits(1_000_000_000)

for i in range(1,1000):
    point = 0
    print('I =', i)
    list = []
    list.append(i)
    while True:
        if len(list) >= 16:
            break
        y = list[-1]
        z = -y**2-y+1
        list.append(z)
        if point == 1:
            break
        for j in list[:-1]:
            x = gcd(j, z)

            if x != 1:
                print('(',list.index(j)+1,')','\n','(',list.index(z)+1,')','\ngcd=',x,'\n')
                point = 1
                exit()
time()
