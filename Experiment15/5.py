class Student:
    def __init__(self, name, age):    #CRATING FUNCTION USING CONSTRUCTOR
        self.name = name         #ASSIGNING VALUES
        self.age = age

#CREATING OBJECT
s1 = Student("Aman", 19)       
s2 = Student("Riya", 21)

print("Student 1 - Name:", s1.name, "Age:", s1.age)
print("Student 2 - Name:", s2.name, "Age:", s2.age)