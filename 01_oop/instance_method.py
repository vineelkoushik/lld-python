#Instance Methods
class Abc:
    #An instance method is a method that works with an object's data (instance attributes).
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def update_age(self,new_age):
        self.age = new_age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
s1=Abc("Oggy", 25)
s2=Abc("Olivia", 30)
s1.display_info()
s2.display_info()
s1.update_age(34) # Updating an instance attribute using an instance method
s1.display_info()