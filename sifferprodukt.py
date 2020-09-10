n = input()
while len(n) != 1:
    total = 1
    for i in range(len(n)):
        if n[i] != "0":
            total *= int(n[i])
    n = str(total)
print(n)
