import itertools

n=3
combinations = list(itertools.combinations(range(n), 1))
print(combinations)
for x in combinations:
    print(x[0])