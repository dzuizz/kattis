X, Y, N = map(int, input().split())
for i in range(1, N + 1):
    s = ""
    if i % X == 0:
        s += "Fizz"
    if i % Y == 0:
        s += "Buzz"
    if s == "":
        s = i
    print(s)
