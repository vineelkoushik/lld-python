#Static Method
#A static method is a method defined inside a class 
#that does not depend on instance attributes or class attributes
#Unlike instance methods and class methods,
#a static method does not receive self or cls automatically
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b
print(Calculator.add(10, 20))
print(Calculator.multiply(5, 4))