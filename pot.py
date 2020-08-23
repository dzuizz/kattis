n = int(input())
t = 0
for i in range(n):
    n = int(input())
    ln = n%10
    n = (n-ln)/10
    t += n ** ln
print(int(t))
