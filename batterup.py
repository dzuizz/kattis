n = int(input())
l = list(map(int, input().split()))
numerator = 0
denominator = 0
for i in range(n):
    if int(l[i]) != -1:
        numerator += int(l[i])
        denominator += 1

print(numerator/denominator)
