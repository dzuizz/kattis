t = int(input())
for i in range(t):
    b, p = map(float, input().split())
    minabpm = 60 / (p / (b-1))
    bpm = (60*b) / p
    maxabpm = 60 / (p / (b+1))
    print(minabpm, bpm, maxabpm)
