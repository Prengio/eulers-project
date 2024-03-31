def num_digits(n):
    return len(str(n))


digits = []
x = 1
y = 2
temp = 0
while num_digits(y)<1000:
    digits.append(y)
    temp = y
    y = y + x
    x = temp
print(len(digits)+3)