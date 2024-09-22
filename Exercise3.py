number: int = int(input('enter a num '))
for row in range( 1 , number + 1):
    for col in range(1, row + 1):
        if row % 2 == 0:
            continue
        print(" " ,col, end="")
    print()
for row in range(number - 1, 0, -1):
    for col in range( 1 , row + 1):
        if row % 2 == 0:
            continue
        print(" " ,col, end="")
    print()
