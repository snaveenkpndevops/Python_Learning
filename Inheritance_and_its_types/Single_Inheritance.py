# Single Inheritance
# Let's consider there is a father and a son. Here son has all rights to use the father wealth (money, car, home, business etc.)

class father():

    def money(self):
        print ("Dad's money....")

    def car(self):
        print ("Dad's Car....")

# Here Son class inherits from the father class 
class son(father):

    def bike(self):
        print ("son's bike")


jackie=son()
jackie.money()    # o/p:  Dad's money....
jackie.car()      # o/p:  Dad's Car....
jackie.bike()     # o/p:  son's bike