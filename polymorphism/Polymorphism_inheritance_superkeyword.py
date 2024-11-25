# Example: Combination of Inheritance + Polymorphism + Super Keyword.

class Employee():
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Manager(Employee):

    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

    def display(self):
        print(f"{self.name} age is {self.age} and his monthly salary is {self.salary}")


person1=Manager("naveen", 25, 90000)
person1.display()   # O/P:   naveen age is 25 and his monthly salary is 90000