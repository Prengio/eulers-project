def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    digits = list(str(n))
    if digits == list(reversed(digits)):
        return True


# only works for numbers bigger than 1
def num_factors(n):
    factors = 2
    if n == 1:
        return 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors += 2
    return factors

def permutation(elements):
    return 'todo'