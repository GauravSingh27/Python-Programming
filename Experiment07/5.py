
n = int(input("Enter number of persons (n): "))

persons = {}
for i in range(n):
    name = input(f"Enter name {i+1}: ").strip()
    city = input(f"Enter city for {name}: ").strip()
    persons[name] = city

print("\na. All names:")
for name in persons.keys():
    print(name)

print("\nb. All cities:")
for city in persons.values():
    print(city)

print("\nc. Name:City pairs:")
for name, city in persons.items():
    print(f"{name}: {city}")

city_count = {}
for city in persons.values():
    city_count[city] = city_count.get(city, 0) + 1

print("\nd. Count of persons in each city:")
for city, count in city_count.items():
    print(f"{city}: {count}")
