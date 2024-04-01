import func

n = 8
primes = [i for i in func.Sieve_Of_Eratosthenes(10**n) if i!= 0 if i!= 1 if len(str(i)) == n]
print(len(primes))

func.time()