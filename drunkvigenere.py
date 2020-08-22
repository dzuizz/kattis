C = list(input())
K = list(input())
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = ""
for x in range(len(C)):
    if x%2 ==0:
        C[x] = a[(a.index(C[x]) - a.index(K[x])) % 26]
    else:
        C[x] = a[(a.index(C[x]) + a.index(K[x])) % 26]

# for every character in C
#   check if even or odd position
#   if even, shift backward according to the corresponding letter in K
#      find corresponding letter in K
#      convert to number, A --> 0, Z --> 25
#      shift the letter in C accordingly

print("".join(C))
