# hybrid Inheritance
# This inheritance is a combination of any two or more inheritance. In the example, we are going to see the combination of multiple + hierarchical inheritance.
# Let's consider there is a father, son1, son2 and son3. Here son's has all rights to use their father wealth (money, car, home, business etc.).  [hierarchical inheritance]
# And son1 also has additional benefit that he can inherit from land class also.  [multiple inheritance]

class father():
    def money(self):
        print ("Dad's money....")

class land():
    def land(self):
        print("Farm house land in ECR...")

class son1(father, land):
    def bike(self):
        print ("first son's bike")

class son2(father):
    def gold(self):
        print ("second son's gold")

class son3(father):
    def laptop(self):
        print ("third son's laptop")

jackie=son1()
jackie.money()   # o/p:  Dad's money....
jackie.land()    # o/p:  Farm house land in ECR...
jackie.bike()    # o/p:  first son's bike

tony=son2()
tony.money()     # o/p:  Dad's money....
tony.gold()      # o/p:  second son's gold

lee=son3()
lee.money()      # o/p:  Dad's money....
lee.laptop()     # o/p:  third son's laptop