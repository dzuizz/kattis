t = int(input())
d = {}
for _ in range(t):
    sound = list(input().split())
    while True:
        l = list(input().split())
        if l != ['what', 'does', 'the', 'fox', 'say?']:
            d[l[0]]= l[2]
        else:
            break

    for v in d.values():
        while v in sound:
            sound.remove(v)
    print(" ".join(sound))
