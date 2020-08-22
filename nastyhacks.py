n = int(input())
for i in range(n):
    r, e, c = map(int, input().split())
    p = e - c
    if p > r:
        print("advertise")
    elif p == r:
        print("does not matter")
    else:
        print("do not advertise")
