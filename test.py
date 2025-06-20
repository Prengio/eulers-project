A = list('UDDDUdddDDUDDddDdDddDDUDDdUUDd')

n = 10**15
for i in A:
    if i == 'D':
        n=n/3
    elif i == 'U':
        n= (4*n+2)/3
    elif i == 'd':
        n= (2*n-1)/3
print(n)