while True:
    try:
        n1, n2 = map(int, input().split())
        print(abs(n1 - n2))
    except EOFError:
        break
