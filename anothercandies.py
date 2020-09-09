t = int(input())
for _ in range(t):
    total = 0
    n = input()
    students = int(input())
    for x in range(students):
        c = int(input())
        total += c
    if total % students == 0:
        print("YES")
    else:
        print("NO")
