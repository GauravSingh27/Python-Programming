even_nums, odd_nums = [], []
with open('numbers.txt', 'r') as src:
    for line in src:
        num = int(line.strip())
        if num % 2 == 0:
            even_nums.append(str(num))
        else:
            odd_nums.append(str(num))

with open('even.txt', 'w') as even_file:
    even_file.write('\n'.join(even_nums))
with open('odd.txt', 'w') as odd_file:
    odd_file.write('\n'.join(odd_nums))
print("Even numbers → even.txt, Odd numbers → odd.txt")