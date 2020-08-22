n = input()
l = list(map(int, input().split()))
x = 0
for i in l:
    if i < 0:
        x += 1
print(x)
