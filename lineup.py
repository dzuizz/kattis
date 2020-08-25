t = int(input())
l = []
for i in range(t):
    e = input()
    l.append(e)
la = l.copy()
ld = l.copy()
la.sort()
ld.sort(reverse = True)
if l == la:
    print("INCREASING")
elif l == ld:
    print("DECREASING")
else:
    print("NEITHER")
