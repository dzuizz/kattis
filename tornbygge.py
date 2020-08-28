n = int(input())
t = 1
l = list(map(int, input().split()))
p = max(l)
for i in range(n):
    c = l[i]
    if c > p:
        t += 1
    p = c

print(t)
