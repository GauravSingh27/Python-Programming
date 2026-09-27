class Employee:
    def __init__(self, name, salary):   #CREATING FUNCTION USING CONSTRUCTOR
        self.name = name        #ASSIGNING VALUES
        self.salary = salary

e1 = Employee("Rahul", 50000)    #CREATING OBJECT
print("Name:", e1.name)
print("Salary:", e1.salary)