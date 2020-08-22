l, x = map(int, input().split())
p = 0
g = 0
for i in range(x):
    a = input().split()
    s = a[0]
    n = int(a[1])
    if s == "enter":
        p += n
        if p > l:
            p -= n
            g += 1
    else:
        p -= n
print(g)
