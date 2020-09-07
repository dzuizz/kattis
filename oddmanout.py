t = int(input())
for x in range(t):
    l = []
    n = int(input())
    s = list(input().split())
    for i in range(len(s)):
        if s[i] not in l:
            l.append(s[i])
        else:
            l.remove(s[i])
    print(f"Case #{x+1}: {l[0]}")
