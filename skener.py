r, c, xr, xc = map(int, input().split())
l = []

for i in range(r):
    l.append(list(input()))

for i in range(len(l)):
    for y in range(xr):
        s = ""
        for u in range(c):
            s += str(l[i][u])*xc
        print(s)
