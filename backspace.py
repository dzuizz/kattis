s = input()
word = []
for i in range(len(s)):
    if s[i] == "<":
        word.pop()
    else:
        word.append(s[i])

print("".join(word))
