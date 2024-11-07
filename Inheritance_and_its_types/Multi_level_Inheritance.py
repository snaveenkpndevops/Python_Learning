# Multi-level Inheritance
# Let's consider there is a father, grandfather and a son. Here son has all rights to use the father and grandfather wealth (money, car, home, business etc.).
# And father has all rights to use his father wealth (money, car, home, business etc.).

class grandfather():

    def land(self):
        print("grandpa's land....")

class father(grandfather):

    def money(self):
        print ("Dad's money....")

class son(father):

    def bike(self):
        print ("son's bike")


lee=father()
lee.land()       # o/p:  grandpa's land....
lee.money()      # o/p:  Dad's money....

jackie=son()
jackie.land()    # o/p:  grandpa's land....
jackie.money()   # o/p:  Dad's money....
jackie.bike()    # o/p:  son's bike