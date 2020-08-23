n = int(input())
for i in range(n):
    s = ""
    c1 = input()
    c2 = input()
    for i in range(len(c1)):
        if c1[i] == c2[i]:
            s += "."
        else:
            s += "*"
    print(c1)
    print(c2)
    print(s)
    print()
