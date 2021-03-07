l = list(map(int, input().split()))
n = 1
for i in range(3):
    n *= l[i]
print(n)
