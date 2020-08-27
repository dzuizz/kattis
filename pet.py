import operator

d = {}
for i in range(1, 6):
    p = list(map(int, input().split()))
    d[i]= sum(p)

m = max(d.items(), key = operator.itemgetter(1))[0]
found = False
while found != True:
    for k, v in d.items():
        if k == m:
            print(k, v)
            found = True
