while True:
    try:
        line = input().lower()
        if "problem" in line:
            print("yes")
        else:
            print("no")
    except EOFError:
        break
