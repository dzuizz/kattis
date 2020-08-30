a, b, c, n = map(int, input().split())
if n >= 3 and a > 0 and b > 0 and c > 0 and a + b + c >= n:
    print("YES")
else:
    print("NO")
