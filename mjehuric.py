l = list(input().split())
while l != ["1", "2", "3", "4", "5"]:
    if int(l[0]) > int(l[1]):
        l[0], l[1] = l[1], l[0]
        print(" ".join(l))
    if int(l[1]) > int(l[2]):
        l[1], l[2] = l[2], l[1]
        print(" ".join(l))
    if int(l[2]) > int(l[3]):
        l[2], l[3] = l[3], l[2]
        print(" ".join(l))
    if int(l[3]) > int(l[4]):
        l[3], l[4] = l[4], l[3]
        print(" ".join(l))
