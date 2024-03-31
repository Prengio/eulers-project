# find the first triangular number to have more than 500 factors
# only need to go up to the square root of the number and add 2 as it is a factor pair

def num_factors(n):
    factors = 2
    if n == 1:
        return 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors += 2
    return factors


n = 0
i = 1
while num_factors(n) < 500:
    n = (i * (i + 1) / 2)
    i += 1
print(n)
