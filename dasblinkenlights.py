import math
p, q, s = map(int, input().split())
lcm = (q / math.gcd(p, q)) * p
if lcm <= s:
    print("yes")
else:
    print("no")
