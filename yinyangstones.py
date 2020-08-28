s = input()
d = {
    "W" : 0,
    "B" : 0
}
for i in range(len(s)):
    v = d.get(s[i])
    d[s[i]]= v + 1

if d.get("W") == d.get("B"):
    print("1")
else:
    print("0")
