name = "PER"
s = input()
n = 0
for i in range(len(s)):
    if s[i] != name[i%3]:
        n += 1

print(n)
