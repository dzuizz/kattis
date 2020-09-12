from collections import defaultdict
n = int(input())
d = defaultdict(int)
c = 0
for i in range(n):
    d[input()]+= 1
for i in range(n):
    a = input()
    if a in d:
        c += 1
        d[a]-= 1
        if d[a] == 0:
            del d[a]

print(c)
