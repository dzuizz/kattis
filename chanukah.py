for i in range(int(input())):
    l = list(map(int, input().split()))
    print(str(l[0])+" "+str((l[1]*(l[1]+1)//2+l[1])))
