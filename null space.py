import numpy as np
from scipy.linalg import null_space

def find_duplicates_with_indexes(lst):
    duplicates = {}
    seen = {}

    for index, value in enumerate(lst):
        if value in seen:
            if value not in duplicates:
                duplicates[value] = [seen[value]]
            duplicates[value].append(index)
        else:
            seen[value] = index

    return duplicates

lst = []

for i in range(2, 20):
    m=1
    n=i
    A = np.matrix([[m,n,-m,-n] , [n,m,n,m]])
    N = null_space(A)
    #print(N)
    x = sum(abs(N[0:,0]))
    lst.append(round(x,3))


print(find_duplicates_with_indexes(lst))
print(lst)