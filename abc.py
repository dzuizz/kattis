l = sorted(list(map(int, input().split())))
o = input()
nl = []
A = l[0]
B = l[1]
C = l[2]
for i in o:
    if i == "A":
        nl.append(A)
    elif i == "B":
        nl.append(B)
    else:
        nl.append(C)
print(nl[0], nl[1], nl[2])
