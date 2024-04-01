import func
from time import process_time


primes = []
for i in range(1, 10_000_001, 2):
    if func.is_prime(i) == True:
        primes.append(i)

print (primes, '\n')
print (len(primes))
print (process_time())