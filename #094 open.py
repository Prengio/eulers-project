import func

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5

n=0
for i in range(1, 333_333_333):
    if heron(i,i,i+1)%1 == 0:
        n+=3*i+1
    if heron(i, i, i-1)%1 == 0:
        n+=3*i-1


print(n-2)
func.time()