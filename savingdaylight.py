while True:
    try:
        ans = []
        l = list(input().split())
        ans.append(l[0])
        ans.append(l[1])
        ans.append(l[2])
        start = list(map(int, l[3].split(":")))
        end = list(map(int, l[4].split(":")))
        start = (start[0]*60) +  start[1]
        end = (end[0]*60) +  end[1]
        dif = end - start
        ans.append(f"{dif//60} hours")
        dif = dif % 60
        ans.append(f"{dif} minutes")
        print(" ".join(ans))
    except EOFError:
        break
