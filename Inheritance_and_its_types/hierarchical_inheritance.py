# hierarchical Inheritance
# Let's consider there is a father, son1, son2 and son3. Here son's has all rights to use their father wealth (money, car, home, business etc.).

class father():
    def money(self):
        print ("Dad's money....")

class son1(father):
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
jackie.bike()    # o/p:  first son's bike

tony=son2()
tony.money()     # o/p:  Dad's money....
tony.gold()      # o/p:  second son's gold

lee=son3()
lee.money()      # o/p:  Dad's money....
lee.laptop()     # o/p:  third son's laptop