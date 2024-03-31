#sum the even fibonacci terms up to 4,000,000
sums = []
x=1
y=2
temp =0
while y<4000000:
    if y%2==0:
        sums.append(y)
    temp=y
    y=y+x
    x=temp
print(sum(sums))
