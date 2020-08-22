x = int(input())
n = int(input())
t = 0
for i in range(n):
    m = int(input())
    t += (x - m)
t += x 
print(t)
