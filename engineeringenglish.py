l = []
while True:
    try:
        ans = []
        s = list(input().split())
        for i in range(len(s)):
            if s[i].lower() in l:
                ans.append(".")
            else:
                ans.append(s[i])
                l.append(s[i].lower())
        print(" ".join(ans))
    except EOFError:
        break
