d = {}
for i in range(10):
    a = int(input())
    m = a % 42
    if m not in d:
        d[m]= ""
print(len(d))
