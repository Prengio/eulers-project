# 19 digit square that ends in 0 cause it's square ends in 0

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = [1,2,2,3,3,2,4,6,5,7,6,3,7,4,8,4,9]

#digits[0:9]) == print(temp[0:18:2]):

for i in range(10**9, 3162277661, 10):
   if digits[0:9] == list(str(i**2))[0:18:2]:
       print(i)
