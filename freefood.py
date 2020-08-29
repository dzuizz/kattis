n = int(input())
l = []
for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        if i not in l:
            l.append(i)
print(len(l))
