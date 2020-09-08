t = int(input())
for _ in range(t):
    l = []
    n = int(input())
    for i in range(n):
        l.append(int(input()))
    wvote = max(l)
    if l.count(wvote) > 1:
        print("no winner")
    elif wvote > sum(l)/2:
        print(f"majority winner {l.index(wvote)+1}")
    else:
        print(f"minority winner {l.index(wvote)+1}")
