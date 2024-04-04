import func
primes = [x for x in func.Sieve_Of_Eratosthenes(10000) if x != 0]

print(primes)
trunc= []

for x in primes:
    n = len(str(x))
    par = True
    temp = x
    while n > 1 and par == True:
        temp = int(str(temp)[0:-1])
        if temp not in primes or temp == 1:
            par = False
        n-=1
    if par == True:
        trunc.append(x)
print(trunc)
for x in trunc:
    n = len(str(x))
    par = True
    temp = x
    while (n > 1 and par == True):
        temp = int(str(temp)[1:])
        if temp not in primes or temp == 1:
            par = False
        n-=1
    if par == False:
        trunc.remove(x)

print(trunc)