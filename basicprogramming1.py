n, t = map(int, input().split())
a = list(map(int, input().split()))

if t == 1:
    print(7)

elif t == 2:
    if a[0] > a[1]:
        print("Bigger")
    elif a[1] == a[0]:
        print("Equal")
    else:
        print("Smaller")

elif t == 3:
    l = a[:3]
    l.sort()
    print(l[1])

elif t == 4:
    total = 0
    for i in range(n):
        total += a[i]
    print(total)

elif t == 5:
    total = 0
    for i in range(n):
        if a[i] % 2 == 0:
            total += a[i]
    print(total)

elif t == 6:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(n):
        a[i] = alphabet[a[i]%26]
    print("".join(a))

else:
    i = 0
    x = 0
    while True:
        i = a[i]
        if x == n:
            print("Cyclic")
            break

        if i > n-1 or i < 0:
            print("Out")
            break

        elif i == n-1:
            print("Done")
            break

        else:
            x += 1
            continue
