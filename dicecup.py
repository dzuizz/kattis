n, m = map(int, input().split())
s = {}
for x in range(1, n+1):
    for y in range(1, m+1):
        sum = x + y
        if sum in s:
            v = s.get(sum)
            s[sum]= v+1
        else:
            s[sum]= 1
for i in s:
    val = s.get(i)
    if val == max(s.values()):
        print(i)
