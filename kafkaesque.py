t = int(input())
previous = 0
count = 1
for i in range(t):
    n = int(input())
    if n < previous:
        count += 1
    previous = n

print(count)
