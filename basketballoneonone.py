s = input()
d = {
    "A" : 0,
    "B" : 0
}
x = 3
for i in range(len(s)):
    if i % 2 == 0:
        r = s[i:i+x]
        v = d.get(r[0])
        d[r[0]]= v + int(r[1])
        x += 2

v = list(d.values())
k = list(d.keys())
print(k[v.index(max(v))])
