import itertools

length = {0}
f = int(input())
fuse = []
for i in range(f):
    fuse.append(int(input()))

#orders = list(permutations(fuse, f))
#print(comb)

c = [0, -0.5, 0.5, -1, 1]
comb = [p for p in itertools.product(c, repeat=f)]
if f == 1:
    n = fuse[0]
    length.add(n/2)
    length.add(n)
if f != 1:
    for coeff in comb:
        z=0
        for i in range(f):
            z = z+coeff[i]*fuse[i]
        if z >= 0:
            length.add(z)
            if z == 0.25:
                print(coeff)
            if 1 in coeff:
                if -0.5 or 0.5 in coeff:
                    z=z/2
                    length.add(z)


print(len(length))