from num2words import num2words
length = []
for i in range(1, 1001):
    length.append(len(num2words(i).replace(" ", "").replace("-", "")))

print(sum(length))