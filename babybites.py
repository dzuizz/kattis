n = int(input())
l = list(input().split())
previous = 0
s = "makes sense"
for i in range(n):
    if l[i] == "mumble":
        c = previous + 1
    else:
        c = int(l[i])
    if c != previous + 1:
        s = "something is fishy"
        break
    previous += 1

print(s)
