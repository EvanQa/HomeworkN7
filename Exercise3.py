#my solution
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

#teacher solution
max_line: int = 0
while max_line % 2 == 0:
    max_line: int = int(input('max line'))

for number in range(1, max_line + 2, 2):
    spaces: int =  (max_line - number) // 2
    print(' ' * spaces)
    for i in range( 1, number + 1):
        print(i, end="")


for number in range(max_line - 2, 1 - 2, -2):
    spaces: int =  (max_line - number) // 2
    print(' ' * spaces)
    for i in range(1, number + 1):
        print(i, end="")