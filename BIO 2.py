import numpy as np
n = int(input())
r = int(input())
g = int(input())
grid = [[0]*n]*n


def pos(x):
    c = []
    c.append(int(x//n))
    c.append(int(x%n-1))
    return c

def val(x):
    return (x[0]*n+x[1]+1)

grid[0][0] = 1
rpos = [0,0]
for a in range(3):
    gtemp = pos(val(rpos)+g)
    #print(gtemp[0])
    grid[3][2] = 2

print(2,1)

