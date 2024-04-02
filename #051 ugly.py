import func
import copy
import itertools
# this is probably some of the worst code you will see
# the code takes 15 minutes to run and need to be manually changed for different numbers of digits
n=6
m = 8
primes = [i for i in func.Sieve_Of_Eratosthenes(10 ** n) if i != 0 if i != 1 if len(str(i)) == n]
permanent_primes = []
for i in primes:
    permanent_primes.append(list(str(i)))
permanent_primes = tuple(permanent_primes)


combinations = list(itertools.combinations(range(n), 1))
for x in combinations:
    primes_list = copy.deepcopy(permanent_primes)
    # the first number is the prime and second the digit(-1 form both)
    for i in range(len(primes_list)):
        primes_list[i][x[0]] ='*'

    dup = set()    # a set of the reduced primes with at least 8 instances
    for i in primes_list:
        if primes_list.count(i) > m-1:
            dup.add(tuple(i))
    if len(dup) > 0:
        print(dup)

combinations = list(itertools.combinations(range(n), 2))
for x in combinations:
    primes_list = copy.deepcopy(permanent_primes)
    # the first number is the prime and second the digit(-1 form both)
    for i in range(len(primes_list)):
        if primes_list[i][x[0]] == primes_list[i][x[1]]:
            primes_list[i][x[0]] ='*'
            primes_list[i][x[1]] ='*'

    dup = set()    # a set of the reduced primes with at least 8 instances
    for i in primes_list:
        if primes_list.count(i) > m-1:
            dup.add(tuple(i))
    if len(dup) > 0:
        print(dup)

combinations = list(itertools.combinations(range(n), 3))
for x in combinations:
    primes_list = copy.deepcopy(permanent_primes)
    # the first number is the prime and second the digit(-1 form both)
    for i in range(len(primes_list)):
        if primes_list[i][x[0]] == primes_list[i][x[1]] == primes_list[i][x[2]]:
            primes_list[i][x[0]] ='*'
            primes_list[i][x[1]] ='*'
            primes_list[i][x[2]] ='*'

    dup = set()    # a set of the reduced primes with at least 8 instances
    for i in primes_list:
        if primes_list.count(i) > m-1:
            dup.add(tuple(i))
    if len(dup) > 0:
        print(dup)

combinations = list(itertools.combinations(range(n), 4))
for x in combinations:
    primes_list = copy.deepcopy(permanent_primes)
    # the first number is the prime and second the digit(-1 form both)
    for i in range(len(primes_list)):
        if primes_list[i][x[0]] == primes_list[i][x[1]] == primes_list[i][x[2]] == primes_list[i][x[3]]:
            primes_list[i][x[0]] ='*'
            primes_list[i][x[1]] ='*'
            primes_list[i][x[2]] ='*'
            primes_list[i][x[3]] ='*'

    dup = set()    # a set of the reduced primes with at least 8 instances
    for i in primes_list:
        if primes_list.count(i) > m-1:
            dup.add(tuple(i))
    if len(dup) > 0:
        print(dup)

combinations = list(itertools.combinations(range(n), 5))
for x in combinations:
    primes_list = copy.deepcopy(permanent_primes)
    # the first number is the prime and second the digit(-1 form both)
    for i in range(len(primes_list)):
        if primes_list[i][x[0]] == primes_list[i][x[1]] == primes_list[i][x[2]] == primes_list[i][x[3]] == primes_list[i][x[4]]:
            primes_list[i][x[0]] ='*'
            primes_list[i][x[1]] ='*'
            primes_list[i][x[2]] ='*'
            primes_list[i][x[3]] ='*'
            primes_list[i][x[4]] ='*'

    dup = set()    # a set of the reduced primes with at least 8 instances
    for i in primes_list:
        if primes_list.count(i) > m-1:
            dup.add(tuple(i))
    if len(dup) > 0:
        print(dup)



#print(primes_list)
#print(len(primes))
#print(len(primes_list))
func.time()
