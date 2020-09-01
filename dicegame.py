g = 0
e = 0
l = list(map(int, input().split()))
g += sum(l)
l = list(map(int, input().split()))
e += sum(l)
if e > g:
    print("Emma")
elif g > e:
    print("Gunnar")
else:
    print("Tie")
