numbers = [1, 2, 2, 3, 2, 4, 5, 2]
countn = numbers.count(2)
print(countn) 


#with loopsss
numbers = [1, 2, 2, 3, 2, 4, 5, 2]
target = 2
count = 0

for num in numbers:
    if num == target:
        count += 1

print(f"{target} appears {count} times") 
