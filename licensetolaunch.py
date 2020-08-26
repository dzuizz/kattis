n = int(input())
l = list(map(int, input().split()))
m = min(l)
for i in range(n):
    if l[i] == m:
        print(i)
        break
