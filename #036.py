import func

def binary(n):
    if list(bin(n)[2:]) == list(reversed(bin(n)[2:])):
        return True



palindromes = []
for n in range(1, 1_000_000):
    if func.is_palindrome(n) == True and binary(n) == True:
        palindromes.append(n)



print(sum(palindromes))
func.time()
