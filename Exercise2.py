#my solution
world_record = 6.23
good_results_count = 0
good_results_sum = 0
highest_result = 0
record_holder = None

for i in range(7):
    result = float(input(f" enter result {i + 1} : "))
    if result < 5.80:
        continue

    good_results_count += 1
    good_results_sum += result


    if result > world_record:
        world_record = result
        record_holder = input(f" New highest result in the world! Enter name of athlete :  ")


    if result > highest_result:
        highest_result = result

if good_results_count > 0:
    print(f"Number of good results: {good_results_count}")
    print(f"Average of good results: {good_results_sum / good_results_count:.2f} meters")
    print(f"Highest result: {highest_result} meters")
else:
    print("No valid results.")

if record_holder:
    print(f"New world record: {world_record} meters by {record_holder}")
else:
    print("None")

#teacher solution
WORLD_RECORD: float = 6.23
new_world_record: float = None
new_world_record_name: str = None
count_good_result: int = 0
sum_good_result: int = 0
max_score: float = None
MAX_COUNT: int = 7
for _ in range(MAX_COUNT):
    result: float = float(input("whats the height?"))
    if result < 5.80:
        continue
    count_good_result += 1
    sum_good_result = result
    if not max_score is None or result > max_score:
        max_score = result
    if result > WORLD_RECORD:
        new_world_record =result
        new_world_record_name = input('whats the name of the jumper?')
else:
    avg_good_score: float = None
    if count_good_result:
        avg_good_score: float = sum_good_result / count_good_result
    print(f"highest score: {max_score}")
    if new_world_record:
        print(f" new world record height: {new_world_record}")
        print(f" new world record jumper name: {new_world_record_name}")
    else:
        print("no new record achieved. None")