import func
import numpy as np
import plotly.graph_objects as go

coeff = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
x = range(1, len(coeff))
y = np.poly1d(coeff)(x)
print(y)

sum = 0
for i in range(1, len(coeff)):
    op = func.lagrange(x[:i], y[:i])
    sum += np.polyval(op, i+1)
    print(op)

print(round(sum))