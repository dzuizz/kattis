n = 0
while n != -1:
    m = 0
    t = 0
    n = int(input())
    for i in range(n):
        s, tc = map(int, input().split())
        m += s * (tc - t)
        t = tc
    if m != 0:
        print(f"{m} miles")
