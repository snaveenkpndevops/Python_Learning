# Multiple Inheritance
# Let's consider there is a father, mother and a son. Here son has all rights to use the father and mother wealth (money, car, home, business etc.)

class dad():

    def money(self):
        print ("Dad's Money.....")


class mom():

    def gold(self):
        print ("Mom's Gold jewel.....")

# Here Son class inherits from the father and mother class 
class son(dad, mom):

    def bike(self):
        print ("Son's Bike.....")


jackie=son()
jackie.money()    # o/p:  Dad's Money.....
jackie.gold()     # o/p:  Mom's Gold jewel.....
jackie.bike()     # o/p:  Son's Bike.....