nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
s = input()
p = input()
for _ in range(1):
    if (s == p) or (s[1:] == p and s[0] in nums) or (s[:-1] == p and s[-1] in nums) or (s == p.swapcase()):
        print("Yes")
    else:
        print("No")
