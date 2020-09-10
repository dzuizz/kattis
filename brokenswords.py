t = int(input())
tb = 0
lf = 0
for i in range(t):
    n = input()
    tb += 2 - (int(n[0]) + int(n[1]))
    lf += 2 - (int(n[2]) + int(n[3]))

swords = min(tb, lf)
swords = swords//2
tbx = tb - swords*2
lfx = lf - swords*2
print(swords, tbx, lfx)
