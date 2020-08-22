T = int(input())
for i in range(T):
    N = int(input())
    num = 1
    for x in range(1, N + 1):
        num *= x
    num = num % 10
    print(num)
