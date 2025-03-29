import func

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted_letters = []
encrypted = []
decrypted = []

for i in input().lower():
    encrypted_letters.append(i)
for i in encrypted_letters:
    encrypted.append(letters.index(i))
for i in range(len(encrypted)-1, 0, -1):
    encrypted[i] = (encrypted[i]-encrypted[i-1]-1) % 26

for i in encrypted:
    decrypted.append(letters[i])

delimiter = ""
print(delimiter.join(decrypted).upper())

func.time()
