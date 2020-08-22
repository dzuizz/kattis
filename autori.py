s = input().split('-')
x = 0
name = ""
for e in range(len(s)):
    name += s[x][:1]
    x += 1
print(name)
