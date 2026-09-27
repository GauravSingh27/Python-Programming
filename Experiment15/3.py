class Student:
    def __init__(self, name, age):   #CRATING FUNCTION USING CONSTRUCTOR
        self.name = name      #ASSIGNING VALUES
        self.age = age

s1 = Student("Gaurav", 20)    #OBJECTS
print("Name:", s1.name)
print("Age:", s1.age)