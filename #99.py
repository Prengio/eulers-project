import numpy as np

with open("0099_base_exp.txt", "r") as file:
    data = [tuple(map(int, line.strip().split(","))) for line in file]


x = 0
id = 0
for i in range(len(data)):
    n = data[i][1]*np.log(data[i][0])
    if n>x:
        x = n
        id = i

print(id+1)