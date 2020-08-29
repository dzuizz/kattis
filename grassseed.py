cost = float(input())
l = int(input())
total = 0
for i in range(l):
    width, length = map(float, input().split())
    total += (width*length) * cost
print(total)
