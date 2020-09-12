n = int(input())
odd = False
even = False
done = False
for i in range(100):
    c = 0
    for x in range(n):
        c += i + x
    if c % 2 == 0 and even == False:
        even = True
    elif c % 2 == 1 and odd == False:
        odd = True
if odd == True:
    if even == True:
        print("Either")
    else:
        print("Odd")
else:
    if even == True:
        print("Even")
