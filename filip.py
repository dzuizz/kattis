def change(string):
    return int("".join(list(string[::-1])))

l = input().split()
a = change(l[0])
b = change(l[1])
print(max(a, b))
