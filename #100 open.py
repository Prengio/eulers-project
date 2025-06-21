# n = no of blue and x = no of red. Then solve the quadratic in n. Then use pell equations for the root and find pairs until their sum is as big as needed
import numpy as np

sol = np.array([[3],[1]])
A = np.array([[3,8],[3,1]])

while True:
    sol = np.matmul(A,sol)
    if 2*sol[1][0]+1/2+sol[0][0]/2 >   10**12:
        x = sol[1][0]+1/2+sol[0][0]/2
        y = sol[1][0]
        print((x/(x+y))*(x-1)/(x+y-1))
        exit()
        
def pell_solutions(limit=100):
    m, x = 3, 1
    solutions = [(x, m)]

    for _ in range(limit - 1):
        m, x = 3 * m + 8 * x, m + 3 * x
        solutions.append((x, m))

    return solutions

# Print first 10 solutions
for x, m in pell_solutions(10):
    print(f"x = {x}, m = {m}, check: 8*{x}^2 + 1 = {8*x**2 + 1} = {m}^2")
