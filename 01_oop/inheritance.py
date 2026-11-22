class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("This is the Parent class")
        print(self.a, self.b)
class Child(Parent):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def show_child(self):
        print("This is the Child class")
        print(self.a,self.b,self.c)
c1 = Child(10,20,30)
c1.show_child()
c1.display()