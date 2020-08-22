l = list(input())
p = ""
for i in range(len(l)):
    c = l[i]
    if c == p:
        l[i] = ""
    p = c
print("".join(l))
