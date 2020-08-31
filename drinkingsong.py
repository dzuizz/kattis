n = int(input())
word = input()
while n != 0:
    if n == 1:
        print(f"{n} bottle of {word} on the wall, {n} bottle of {word}.")
        print(f"Take it down, pass it around, no more bottles of {word}.")
        n -= 1
    elif n == 2:
        print(f"{n} bottles of {word} on the wall, {n} bottles of {word}.")
        n -= 1
        print(f"Take one down, pass it around, {n} bottle of {word} on the wall.")
        print()
    else:
        print(f"{n} bottles of {word} on the wall, {n} bottles of {word}.")
        n -= 1
        print(f"Take one down, pass it around, {n} bottles of {word} on the wall.")
        print()
