d = {}
while True:
    l = list(input().split())
    if l == []:
        break
    else:
        d[l[1]]= l[0]

while True:
    try:
        s = input()
        if s in d:
            print(d.get(s))
        else:
            print("eh")
    except EOFError:
        break
