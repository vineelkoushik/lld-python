#Class Attributes
#Class attributes belong to the class itself and are 
# shared by its instances unless an instance overrides them.
#Notice that company is defined outside __init__, directly inside the class.
class Employee:
    company = "Google" # Class attribute
    def __init__(self, name):
        self.name = name # Instance attribute
emp1 = Employee("Oggy")
emp2 = Employee("Olivia")
emp1.company = "Microsoft" # Creates an instance attribute, shadowing the class attribute
print(emp1.company)
print(emp2.company)
print(Employee.company)
Employee.company="Amazon" 
print(emp2.company)
print(emp1.company)
print(Employee.company)