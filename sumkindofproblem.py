p = int(input())
for _ in range(p):
    s1 = 0
    s2 = 0
    s3 = 0
    x = -1
    l = list(map(int, input().split()))
    for i in range(l[1]):
        s1 += i + 1
    for i in range(l[1]):
        x += 2
        s2 += x
    x = 0
    for i in range(l[1]):
        x += 2
        s3 += x
    print(l[0], s1, s2, s3)
