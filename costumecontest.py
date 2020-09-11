d = {}
t = int(input())
for i in range(t):
    c = input()
    if c not in d:
        d[c]= 1
    else:
        d[c]+= 1

temp = min(d.values())
ans = [key for key in d if d[key] == temp]
ans.sort()
for i in range(len(ans)):
    print(ans[i])
