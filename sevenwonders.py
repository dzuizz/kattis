S = input()
P = 0
t = S.count('T')
c = S.count('C')
g = S.count('G')
if 'T' in S and 'C' in S and 'G' in S:
    P += min(t, c, g) * 7
P += t**2 + c**2 + g**2
print(P)
