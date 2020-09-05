n = int(input())
for i in range(n):
    l = []
    s, d = map(int, input().split())
    if s >= d :
        l = ((s-d)//2)+d
        sm = (s-d)//2
        if sm+l == s:
            print(l, sm)
        else:
            print("impossible")
    else:
        print("impossible")
