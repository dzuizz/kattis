vowels = ['a', 'e', 'i', 'o', 'u', 'y']
while True:
    try:
        l = []
        sentence = list(input().split())
        for i in sentence:
            end = ""
            ans = ""
            found = False
            if i[0] in vowels:
                l.append(i + "yay")
            else:
                for x in range(len(i)):
                    if i[x] in vowels and found == False:
                        end = ans
                        ans = i[x]
                        found = True
                    else:
                        ans += i[x]
                l.append(ans + end + "ay")
        print(" ".join(l))
    except EOFError:
        break
