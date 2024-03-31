# largest prime factor of 600851375143
# it is better to just find prime factors of 600851375143 and
# the program will return the final value it finds being the highest one

import math
def largest_prime_factor(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    largest_prime = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime
# Example usage
num = 600851475143
print(largest_prime_factor(num))