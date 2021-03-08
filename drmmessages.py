alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input()
sub1 = message[:(len(message)//2)]
sub2 = message[(len(message)//2):]
word1 = ""
word2 = ""
result = ""
total = 0
for i in range(len(sub1)):
    total += alpha.index(sub1[i])

for i in range(len(sub1)):
    word1 += alpha[(alpha.index(sub1[i])+total)%26]

total = 0
for i in range(len(sub2)):
    total += alpha.index(sub2[i])

for i in range(len(sub2)):
    word2 += alpha[(alpha.index(sub2[i])+total)%26]

for i in range(len(sub1)):
    result += alpha[(alpha.index(word1[i])+alpha.index(word2[i]))%26]

print(result)
