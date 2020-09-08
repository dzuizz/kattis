oned = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
twod = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def convert(num):
    global ans
    length = len(str(num))
    if num == 0:
        ans.append("zero")
    elif length == 1:
        ans.append(oned[num-1])
    elif length == 2:
        tensp = int(str(num)[0])
        onesp = int(str(num)[1])
        if tensp == 1:
            ans.append(teens[onesp])
        elif onesp != 0:
            s = twod[tensp-2] + "-" + oned[onesp-1]
            ans.append(s)
        else:
            s = twod[tensp-2]
            ans.append(s)

while True:
    try:
        ans = []
        line = list(input().split())
        for i in range(len(line)):
            if line[i].isnumeric() == True:
                convert(int(line[i]))
            else:
                ans.append(line[i])
        print(" ".join(ans))
    except EOFError:
        break
