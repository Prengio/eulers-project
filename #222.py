def packing(i):
    sum = i[0] + i[-1]
    for j in range(0, len(i) - 1):
        x = i[j]
        y = i[j + 1]
        sum = sum + (x+y)*(1-(100/(x+y)-1)**2)**0.5
    return sum

spheres = [i for i in range(30, 51)]
pack = [30]
for i in range(1, len(spheres)):
    ball = spheres[i]
    tot = 10000
    for j in range(len(pack)+1):
        pack_temp = pack.copy()
        pack_temp.insert(j, ball)
        if packing(pack_temp) <tot:
            pack_hold = pack_temp.copy()
            tot = packing(pack_hold)
    pack = pack_hold.copy()

print(pack)
print(len(pack))
print(round(packing(pack)*1000))


