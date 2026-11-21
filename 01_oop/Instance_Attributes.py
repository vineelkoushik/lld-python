#Instance Attributes
#Instance attributes are variables that belong to a particular object.
#Each object maintains its own separate values.
class Employee:
    def __init__(self, name, salary):
        self.name = name #Instance attribute
        self.salary = salary #Instance attribute
emp1 = Employee("Oggy", 30000)
emp2 = Employee("Olivia", 40000)
print(emp1.name) 
print(emp2.name)
print(emp1.salary)
print(emp2.salary)