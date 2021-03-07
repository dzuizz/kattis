l = []
for i in range(int(input())):
    l = list(map(int, input().split()))
    print(sum(l[1:l[0]+1])-l[0]+1)
