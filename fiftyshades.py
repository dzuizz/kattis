t = int(input())
c = 0
for i in range(t):
    s = input().lower()
    if "pink" in s or "rose" in s:
        c += 1
if c > 0:
    print(c)
else:
    print("I must watch Star Wars with my daughter")
