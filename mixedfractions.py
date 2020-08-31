while True:
    l = list(map(int, input().split()))
    if l == [0, 0]:
        break
    else:
        whole = l[0] // l[1]
        numerator = l[0] % l[1]
    print(f"{whole} {numerator} / {l[1]}")
