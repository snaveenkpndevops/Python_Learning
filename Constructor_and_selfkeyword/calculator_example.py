# Create a class called calculator
# Create 2 variables a and b
# Create a function called add, sub, mul, div all functions should take 2 variable as parameter.
# pass the a and b value through object().


class calculator:

    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print (f"The addition of {self.num1} and {self.num2} is {self.num1+self.num2}")

    def sub(self):
        print (f"The substraction of {self.num1} and {self.num2} is {self.num1-self.num2}")

    def mul(self):
        print (f"The multiplication of {self.num1} and {self.num2} is {self.num1*self.num2}")

    def div(self):
        print (f"The division of {self.num1} and {self.num2} is {self.num1/self.num2}")


object1=calculator(5,10)
object1.add()                 # o/p:  The addition of 5 and 10 is 15

object2=calculator(20,5)
object2.div()                 # o/p:  The division of 20 and 5 is 4.0

