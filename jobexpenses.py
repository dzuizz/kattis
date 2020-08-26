t = int(input())
e = 0
k = list(input().split())
for i in range(t):
    c = int(k[i])
    if c < 0:
        e -= c
print(e)
