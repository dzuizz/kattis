t = int(input())
for i in range(t):
    l = list(input().split())
    if int(l[1][:4]) >= 2010:
        print(f"{l[0]} eligible")
    elif int(l[2][:4]) >= 1991:
        print(f"{l[0]} eligible")
    elif int(l[3]) >= 41:
        print(f"{l[0]} ineligible")
    else:
        print(f"{l[0]} coach petitions")
