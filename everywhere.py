t = int(input())
for x in range(t):
    cs = []
    n = int(input())
    for y in range(n):
        c = input()
        if c not in cs:
            cs.append(c)
    print(len(cs))
