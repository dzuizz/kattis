t = int(input())
for i in range(t):
    a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    s = input().lower()
    for x in s:
        if x in a:
            a.remove(x)
    if a == []:
        print("pangram")
    else:
        print("missing", "".join(a))
