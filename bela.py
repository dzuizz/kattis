d = {
    "A":[11, 11],
    "K":[4, 4],
    "Q":[3, 3],
    "J":[20, 2],
    "T":[10, 10],
    "9":[14, 0],
    "8":[0, 0],
    "7":[0, 0]
}
l = list(input().split())
total = 0
for i in range(int(l[0])*4):
    card = input()
    if card[1] == l[1]:
        total += d.get(card[0])[0]
    else:
        total += d.get(card[0])[1]

print(total)
