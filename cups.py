t = int(input())
ns = []
for i in range(t):
    l = list(input().split())
    if l[0].isnumeric() == True:
        l[0] = int(l[0]) / 2
        s = [l[0], l[1]]
        ns.append(s)
    else:
        l[1] = int(l[1])
        s = [l[1], l[0]]
        ns.append(s)
ns.sort()
for i in range(len(ns)):
    print("".join(ns[i][1]))
