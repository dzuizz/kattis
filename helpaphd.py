t = int(input())
for i in range(t):
    num = 0
    s = input()
    if "+" in s:
        l = s.split("+")
        for i in range(len(l)):
            num += int(l[i])
        print(num)
    else:
        print("skipped")
