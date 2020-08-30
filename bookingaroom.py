r, n = map(int, input().split())
occupied = []
for i in range(n):
    num = int(input())
    occupied.append(num)

found = False
for i in range(1, r+1):
    if i not in occupied:
        print(i)
        found = True
        break

if found == False:
    print("too late")
