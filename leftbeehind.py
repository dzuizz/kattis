while True:
    l = list(map(int, input().split()))
    if l == [0, 0]:
        break
    elif l[0] + l[1] == 13:
        print("Never speak again.")
    elif l[0] > l[1]:
        print("To the convention.")
    elif l[1] > l[0]:
        print("Left beehind.")
    else:
        print("Undecided.")
