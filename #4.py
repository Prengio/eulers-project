# find the largest palindrome number that is the product of two 3-digit numbers

def is_palindrome(n):
    digits = list(str(n))
    length = len(digits)
    for i in range(0, length // 2):
        if digits[i] != digits[-i - 1]:
            return False
    return n


palindromes = []

# we can assume the range is 900 to 1000 to reduce computation
for i in range(900, 1000):
    for j in range(900, 1000):
        if is_palindrome(i * j) == i * j:
            palindromes.append(i * j)

print(max(palindromes))
