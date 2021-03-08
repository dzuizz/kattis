n = 0
l = list(map(str, input().split(";")))
ll = []
for i in range(len(l)):
    if "-" in l[i]:
        ll = list(map(int, l[i].split("-")))
        n += ll[1]-ll[0]+1
    else:
        n += 1

print(n)
