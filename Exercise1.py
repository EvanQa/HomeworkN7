#my solution
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

#teacher solution
# counter: int  = 0
# positive: int = 0
# negative: int = 0
# zeros: int = 0
# div_7: int = 0
# last_positive: int = None
# last_negative: int = None
# SENTINEL: int = -999
# while counter < 10:
#     number: int = int(input('enter a number'))
#     if number == SENTINEL:
#         break
#     if not -1000 <= number <= 1000:
#         continue
#     counter += 1
#     if number % 7 == 0:
#         div_7 += 1
#     if number > 0:
#         positive += 1
#         last_positive = number
#     elif number < 0:
#         negative += 1
#         last_negative = number
#     else:
#         zeros += 1
# else:
#     print(f"positive  count: {positive}")
#     print(f"negative  count: {negative}")
#     print(f" last negative  count: {last_negative}")
#     print(f"last positive  count: {last_positive}")
#     print(f"divided by 7: {div_7}")
#     print(f"zeros: {zeros}")

