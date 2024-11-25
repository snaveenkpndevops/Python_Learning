# Private Variable

# self.__companyname="Google" is a Private variable. 

# By using __ before variable name. we are making this variable as private variable. 
# So this variable cannot be accessed or modified outside the class. It can be accessed only by parent class.

class company:
    def __init__(self):
        self.__companyname="Google"
    
    def display_companyName(self):
        print (f"The company name is {self.__companyname}")


c1=company()
c1.display_companyName()     # o/p: The company name is Google
print(c1.__companyname)      # o/p: error   (Because this private variable cannot be accessed or modified outside the class.)
