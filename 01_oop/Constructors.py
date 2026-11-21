
# Class named Student
class Student:

    # Constructor to initialize student details
    def __init__(self, name: str, rollno: int, marks: int):

        # Validate marks to ensure they are within the valid range (0-100)
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        # Initialize instance attributes
        self.name: str = name
        self.rollno: int = rollno
        self.marks: int = marks

    # Method to check whether the student has passed or failed
    def is_passed(self) -> bool:
        return self.marks >= 35

    # Method to display student details and result
    def display(self) -> None:
        result = "Pass" if self.is_passed() else "Fail"

        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Marks: {self.marks}")
        print(f"Result: {result}\n")


# Creating objects of the Student class
s1 = Student("Oggy", 419, 88)
# negative marks for jack
s2 = Student("Jack", 420, -34)

# Checking the result and displaying student details
print(s1.is_passed())
s1.display()

print(s2.is_passed())
s2.display()
