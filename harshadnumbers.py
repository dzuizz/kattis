num = int(input())

def check():
    global num
    total = 0
    num = str(num)
    for i in num:
        total += int(i)
    num = int(num)
    if num % total == 0:
        return True
    else:
        num += 1
        return False

while True:
    r = check()
    if r == True:
        print(num)
        break
