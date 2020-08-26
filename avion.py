l = []
for i in range(1, 6):
    s = input()
    if "FBI" in s:
        l.append(str(i))

if l == []:
    print("HE GOT AWAY!")
else:
    print(" ".join(l))
