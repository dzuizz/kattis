w = []
s = list(input().split())
a = "yes"
found = False
for i in range(len(s)):
    if s[i] in w:
        found = True
    else:
        w.append(s[i])
    if found == True:
        a = "no"

print(a)
