g, s, c = map(int, input().split())
total = (g*3) + (s*2) + (c*1)
l = []
if total >= 8:
    l.append('Province')
elif total >= 5:
    l.append('Duchy')
elif total >= 2:
    l.append('Estate')
if total >= 6:
    l.append('Gold')
elif total >= 3:
    l.append('Silver')
elif total >= 0:
    l.append('Copper')

print(" or ".join(l))
