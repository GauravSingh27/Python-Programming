# Input 
n = int(input("Enter number of movies: "))

# Create dictionary 
movies = {}
for i in range(n):
    print(f"\n--- Movie {i+1} Details ---")
    name = input("Movie name: ").strip()
    year = int(input("Year: "))
    director = input("Director: ").strip()
    cost = float(input("Production cost (in crores): "))
    earning = float(input("Collection/Earning (in crores): "))
    
    # Store as nested dictionary
    movies[name] = {
        'year': year,
        'director': director,
        'cost': cost,
        'earning': earning
    }

# a. Print all movie details
print("\n" + "="*50)
print("a. ALL MOVIE DETAILS")
print("="*50)
for name, details in movies.items():
    print(f"Movie: {name}")
    print(f"  Year: {details['year']}")
    print(f"  Director: {details['director']}")
    print(f"  Cost: ₹{details['cost']} Cr")
    print(f"  Earning: ₹{details['earning']} Cr")
    print()

# b. Movies released before 2015
print("b. MOVIES RELEASED BEFORE 2015")
print("-" * 30)
before_2015 = [name for name, details in movies.items() if details['year'] < 2015]
if before_2015:
    for movie in before_2015:
        print(f"- {movie} ({movies[movie]['year']})")
else:
    print("No movies before 2015")

# c. Movies that made profit
print("\nc. PROFITABLE MOVIES")
print("-" * 25)
for name, details in movies.items():
    if details['earning'] > details['cost']:
        profit = details['earning'] - details['cost']
        print(f"- {name}: ₹{profit:.2f} Cr profit")

# d. Movies by particular director
director_name = input("\nEnter director name to search: ").strip().lower()
print(f"\nMovies directed by '{director_name.title()}':")
print("-" * 40)
found = False
for name, details in movies.items():
    if details['director'].lower() == director_name:
        print(f"- {name} ({details['year']})")
        found = True
if not found:
    print("No movies found for this director.")
