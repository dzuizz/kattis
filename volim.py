p = int(input())
n = int(input())
time = 0
found = False
for i in range(n):
    l = list(input().split())
    time += int(l[0])
    if time >= 210:
        found = False
    elif found == False:
        if l[1] == "T":
            p += 1
        else:
            continue
        if p == 9:
            p = 1

print(p)
