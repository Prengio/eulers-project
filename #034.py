import math

for i in range(1, 3628800):  # the largest feasible number
    n = 0
    for x in list(str(i)):
        n += math.factorial(int(x))
    if n == i:
        print(i)
