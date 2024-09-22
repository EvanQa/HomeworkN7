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
