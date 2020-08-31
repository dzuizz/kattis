line = input().split()
n = int(line[0])
w = int(line[1])
h = int(line[2])
ds = w * w + h * h
for i in range(n):
    m = int(input())
    if m*m <= ds:
        print("DA")
    else:
        print("NE")