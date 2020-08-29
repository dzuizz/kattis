w = int(input())
n = int(input())
area = 0
for i in range(n):
    l = list(input().split())
    area += int(l[0]) * int(l[1])

print(area//w)
