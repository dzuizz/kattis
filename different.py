while True:
    try:
        n1, n2 = map(int, input().split())
        print(max(n1, n2) - min(n1, n2))
    except EOFError:
        break
