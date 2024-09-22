negative_count: int = 0
positive_count: int = 0
zero_count: int = 0
dev_by_7:int = 0
last_positive = None
last_negative = None
num: int = 0

for _ in range(10):
    num = int(input("Enter number: "))
    if num < -1000 or num > 1000:
        continue
    if num == - 9999:
        break
    if num > 0:
        positive_count += 1
        last_positive = num
    elif num < 0:
        negative_count += 1
        last_negative = num
    else:
        zero_count += 1

    if num % 7 == 0:
        dev_by_7 += 1
    else:
        print('n\Stats')
        print(f"count of positive num: {positive_count}")
        print(f"count of negative num: {negative_count}")
        print(f"count of zero num: {zero_count}")
        print(f"count of dev by 7 num: {dev_by_7}")
        print(f"last positive num: {last_positive}")
        print(f" last negative num: {last_negative}")
