t = int(input())
for i in range(t):
    c = 0
    y = 0
    l = list(input().split(','))
    for x in range(len(l)):
        if l[-1-x] != "":
            c += int(l[-1-x])*(60**y)
        y += 1
    print(c)
