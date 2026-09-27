try:
    N = int(input("Enter number of students: "))
    if N < 2:
        print("At least 2 scores are required.")
        exit()

    scores = list(map(int, input("Enter scores separated by space: ").split()))

    if len(scores) != N:
        print(f"Error: Expected {N} scores, but got {len(scores)}.")
        exit()

    unique_scores = sorted(set(scores), reverse=True)

    if len(unique_scores) < 2:
        print("No runner-up exists (all scores are the same).")
    else:
        print("Runner-up score is:", unique_scores[1])

except ValueError:
    print("Invalid input. Please enter integers only.")
