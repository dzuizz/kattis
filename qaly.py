n = int(input())
t = 0.0
for i in range(n):
    l = input().split()
    a = float(l[0])
    b = float(l[1])
    t = t + a * b
print(t)