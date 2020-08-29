t = int(input())
for i in range(t):
    a = "Impossible"
    e = list(map(int, input().split()))
    if e[0] + e[1] == e[2] or e[0] + e[2] == e[1] or e[1] + e[2] == e[0]:
        a = "Possible"
    elif e[0] * e[1] == e[2] or e[0] * e[2] == e[1] or e[1] * e[2] == e[0]:
        a = "Possible"
    print(a)
