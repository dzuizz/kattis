y, p = map(str, input().split())
y, p = y.lower(), p.lower()
v = ["a", "i", "o", "u"]
s = y
if y[-2] + y[-1] == "ex":
    s += p
elif y[-1] == "e":
    s += "x"
    s += p
elif y[-1] in v:
    s = s[:-1]
    s += "ex"
    s += p
else:
    s += "ex"
    s += p

print(s)
