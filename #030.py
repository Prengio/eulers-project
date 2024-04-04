sum=0
for i in range(2, 354294):
    n=0
    for x in list(str(i)):
        n+=int(x)**5
    if n == i:
        sum+=i
print(sum)