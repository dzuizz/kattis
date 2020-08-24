t = int(input())
d = {}
for i in range(t):
    uni, tea = map(str, input().split())
    if len(d) < 12:
        if uni not in d:
            d[uni]= tea
for k, v in d.items():
    print(k, v)
