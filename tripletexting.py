s = input()
d = {}
for x in range(3):
    word = len(s)//3
    d[x] = s[word*x:word + word*x]
if d.get(0) == d.get(2):
    print(d.get(0))
elif d.get(0) == d.get(1):
    print(d.get(0))
else:
    print(d.get(1))
