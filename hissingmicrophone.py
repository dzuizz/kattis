s = input()
a = 1
p = ""
for i in s:
    c = i
    if c == p and c == "s":
        a += 1
    p = c
if a >= 2:
    print("hiss")
else:
    print("no hiss")
