startT = list(input().split(":"))
endT = list(input().split(":"))
times = [3600, 60, 1]
startTo = 0
endTo = 0
l = []
for i in range(3):
    startTo += int(startT[i])*times[i]
    endTo += int(endT[i])*times[i]

if startTo < endTo:
    dif = endTo - startTo
else:
    dif = 86400 - (startTo - endTo)

for i in range(3):
    ans = str(dif//times[i])
    if len(ans) == 1:
        l.append("0" + ans)
    else:
        l.append(ans)
    dif = dif % times[i]

print(":".join(l))
