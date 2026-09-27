roll = input("Enter Roll No: ")
name = input("Enter Name: ")
course = input("Enter Course: ")
data = f"Roll No: {roll}\nName: {name}\nCourse: {course}"
f = open('student.txt', 'w') as file:
    file.write(data)
print("student.txt created!")