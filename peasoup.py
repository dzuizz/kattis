n = int(input())
found = False
restaraunt = ""
for _ in range(n):
    l = ['pea soup', 'pancakes']
    items = int(input())
    name = input()
    for i in range(items):
        item = input()
        if item in l:
            l.remove(item)
    if l == [] and found == False:
        restaraunt = name
        found = True

if restaraunt == "":
    print("Anywhere is fine I guess")
else:
    print(restaraunt)
