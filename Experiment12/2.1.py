# Read integers from the file
with open("numbers.txt", "r") as f:
    lines = f.read().splitlines()
    numbers = [int(line.strip()) for line in lines if line.strip()]

if not numbers:
    print("File is empty.")
else:
    # a. Find the max number
    max_num = max(numbers)
    print("Maximum number:", max_num)

    # b. Find average of all numbers
    avg = sum(numbers) / len(numbers)
    print("Average:", avg)

    # c. Count numbers greater than 100
    count_gt_100 = sum(1 for n in numbers if n > 100)
    print("Numbers greater than 100:", count_gt_100)
