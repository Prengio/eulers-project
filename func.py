import math
from time import process_time
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    digits = list(str(n))
    if digits == list(reversed(digits)):
        return True


def num_factors(n):
    factors = 2
    if n == 1:
        return 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors += 2
        if (n**0.5) % 1 == 0:
            factors -= 1
    return factors


def Sieve_Of_Eratosthenes(a):
    primes = [i for i in range(a + 1)]
    p = 2
    while p * p <= a:
        if primes[p] != 0:
            for i in range(p * p, a + 1, p):
                primes[i] = 0
        p += 1
    primes.remove(1)
    return primes


def time():
    print(process_time())

