n = int(input())
for i in range(n):
    s = input()
    if "Simon says" in s:
        s = s.split()
        a = " ".join(s[2:])
        print(a)
