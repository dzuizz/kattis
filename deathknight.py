n = int(input())
loss = 0
for i in range(n):
    s = input()
    if 'CD' in s:
        loss += 1
print(n-loss)
