l = list(input().split())
l[1] = int(l[1])
s = ""
if l[0] == "OCT":
    if l[1] == 31:
        s = "yup"
    else:
        s = "nope"
elif l[0] == "DEC":
    if l[1] == 25:
        s = "yup"
    else:
        s = "nope"
else:
    s = "nope"
print(s)
