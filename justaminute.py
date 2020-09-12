t = int(input())
min = 0
sec = 0
for i in range(t):
    l = list(input().split())
    min += int(l[0])
    sec += int(l[1])

ans = round(sec/(min*60), 9)
if ans <= 1:
    print("measurement error")
else:
    print(ans)
