# just turn the question into a pell equation for the root to the solution of the quadratic and do the recurrence until big enough


m, x = 3, 1
solutions = [(x, m)]

while True:
    m, x = 3 * m + 8 * x, m + 3 * x
    if 2*x+1/2+m/2 > 10**12:
        print(x+1/2+m/2)
        exit()


;