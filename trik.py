l = [1, 0, 0]
def swap(m):
    if m == "A":
        l[0], l[1] = l[1], l[0]
    elif m == "B":
        l[1], l[2] = l[2], l[1]
    else:
        l[0], l[2] = l[2], l[0]

s = input()
for char in s:
    swap(char)
if l[0] == 1:
    print("1")
elif l[1] == 1:
    print("2")
else:
    print("3")
