x = int(input())
y = int(input())
Q = 0
if x > 0:
    Q = 1
    if y < 0:
        Q = 4
else:
    Q = 2
    if y < 0:
        Q = 3
print(Q)
