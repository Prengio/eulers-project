# due to the way the function works, it only works if the digits in the list are in ascending order

import itertools

permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(permutations[999_999])
