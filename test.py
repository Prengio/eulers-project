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
