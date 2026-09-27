# Create city.txt
city_data = """Dehradun 5.78 308.20
Delhi 190 1484
Mumbai 124 603
Bangalore 13.5 741
Chennai 11.9 426"""
with open('city.txt', 'w') as f: f.write(city_data)

# 3a. Display all cities
print("All cities:")
for line in open('city.txt'):
    city, pop, area = line.split()
    print(f"{city}: {pop}L, {area}sqkm")

# 3b. Population > 10 lakhs
print("\nCities > 10L:")
for line in open('city.txt'):
    parts = line.split()
    if float(parts[1]) > 10: print(parts[0])

# 3c. Total area
areas = [float(line.split()[2]) for line in open('city.txt')]
print(f"Total area: {sum(areas):.2f} sqkm")