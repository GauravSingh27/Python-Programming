Name = (input("Enter Name "))
SapID = int(input("Enter SAPID "))
Sem = int(input("Enter Semester "))
Course = (input("Enter Course Name "))
CGPA = float(input("Enter CGPA "))

Marks = []
Marks.append(int(input("PDS ")))
Marks.append(int(input("Python ")))
Marks.append(int(input("English ")))
Marks.append(int(input("Chemistry ")))
Marks.append(int(input("Physics ")))

print("MARKS", Marks)

if(CGPA < 3.4):
    print("F")
elif(CGPA >= 3.5 and CGPA <= 5.0):
    print("C+")
elif(CGPA >= 5.1 and CGPA <=6.0):
    print("B")
elif(CGPA >= 6.1 and CGPA <=7):
    print("B+")
elif(CGPA >= 7.1 and CGPA <=8):
    print("A")
elif(CGPA >= 8.1 and CGPA <=9):
    print("A+")
else:
    print("O")


    print(Name)
    print(Name)
    print(Name)
    print(Name)
    print(Name)