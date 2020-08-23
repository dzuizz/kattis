e, f, c = map(int, input().split())
eb = e + f
x = 0
t = 0
while (eb + x) - c >= 0:
    eb += x
    x = eb % c
    eb -= x
    eb /= c
    t += eb
print(int(t))
