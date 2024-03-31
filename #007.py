def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False


primes = []
i = 2
while True:
    if is_prime(i) != False:
        primes.append(i)
    if len(primes) == 10001:
        print(primes[-1])
        exit()
    i += 1
