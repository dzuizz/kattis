l = list(input().split())
d = {}
for i in range(len(l)):
    if l[i][0] in d:
        v = d.get(l[i][0])
        d[l[i][0]]= v + 1
    else:
        d[l[i][0]]= 1
print(max(d.values()))
