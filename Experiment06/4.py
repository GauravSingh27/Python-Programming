main_str = input("ENTER STRING: ").strip()
sub_str = input("ENTER SUBSTRING: ").strip()

if not main_str or not sub_str:
    print("0") 
else:
    count = 0
    for i in range(len(main_str) - len(sub_str) + 1):
        if main_str[i:i+len(sub_str)] == sub_str:
            count += 1

    print(count)
