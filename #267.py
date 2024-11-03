from decimal import Decimal, getcontext

getcontext().prec = 100
money = Decimal(1)
i = 0
f = Decimal(0.146884) #value of f found by finding function and finding local minima

while money < 1_000_000_000:
    i = i + 1
    money = ((1-f)**(1000-i))*((1+2*f)**i)

from math import comb
probability = []
for x in range(0, 1001):
    probability.append(comb(1000, x) / (2**1000))

other = probability[i:]
print(round(sum(other),12))