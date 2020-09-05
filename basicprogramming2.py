from collections import defaultdict
n, t = map(int, input().split())
a = list(map(int, input().split()))

if t == 1:
    d = {}
    possible = "No"
    for i in range(n):
        if 7777-a[i] in d:
            possible = "Yes"
            break
        else:
            d[a[i]]= ""
    print(possible)
elif t == 2:
    l = {}
    ans = "Unique"
    for i in range(n):
        if a[i] in l:
            ans = "Contains duplicate"
        else:
            l[a[i]]= ""
    print(ans)
elif t == 3:
    d = defaultdict(int)
    ans = -1
    dif = n/2
    for i in range(n):
        d[a[i]]+= 1
        if d[a[i]] > dif:
            ans = a[i]
            break
    print(ans)
elif t == 4:
    if n % 2 == 1:
        a.sort()
        print(a[(n-1)//2])
    else:
        a.sort()
        print(a[(n//2)-1], a[n//2])
else:
    l = []
    for i in range(n):
        if 100 <= a[i] and a[i] <= 999:
            l.append(str(a[i]))
    l.sort()
    print(" ".join(l))
