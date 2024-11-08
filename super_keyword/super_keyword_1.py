# Super Keyword
# Let's consider we have a father class and son class. Both father and son having constructor `def __init__()`. When we create a object for son class.
# It will only call the constructor of son class. It will not call the constructor of father class.
# If son class doesn't have constructor `def __init__()` then it will call the constructor of father class.

# If a child class has constructor then it will print the value of that constructor. if it doesn't have then it will print parent constructor.
# To get the elements from parents to child. for this case we will be using `super keyword`.


class father():

    def __init__(self):
        print ("father name is lee....")
    
    def money(self):
        print ("father's money...")

class son(father):

    def __init__(self):
        # super keyword  -->  This will inherit the parent constructor also
        super().__init__()
    
    def bike(self):
        print ("son's bike...")


jackie=son()      #  o/p:  father name is lee....
jackie.money()    #  o/p:  father's money...
jackie.bike()     #  o/p:  son's bike...