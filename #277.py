A = list('UDDDUdddDDUDDddDdDddDDUDDdUUDd')
A.reverse()

for i in range(20371464, 100000000000): # found the lower bound by unputting 10^15 and finding the number that would result from the steps
    for j in A:
        if j == 'D':
            i=3*i
        elif j == 'U':
            i= ((3*i)-2)/4
            if i%1 != 0:
                break
        elif j == 'd':
            i = ((3*i)+1)/2
            if i%1 != 0:
                break
    if i % 1 == 0:
        print(i)
        exit()
