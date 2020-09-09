n, y = map(int, input().split())
l = []
for i in range(y):
    num = int(input())
    if num not in l:
        l.append(num)
for i in range(n):
    if i not in l:
        print(i)
print(f"Mario got {len(l)} of the dangerous obstacles.")
