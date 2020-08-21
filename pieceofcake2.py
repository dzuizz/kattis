n, h, v = map(int, input().split())
r1 = h*v
r2 = h*(n-v)
r3 = (n-h)*v
r4 = (n-h)*(n-v)
print(max(r1, r2, r3, r4) * 4)
