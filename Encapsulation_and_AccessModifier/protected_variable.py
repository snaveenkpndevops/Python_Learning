# Protected Variable

# self._companyname="Google" is a Protected variable. 

# By using _ before variable name. we are making this variable as Protected variable. 
# So this variable can be accessed by parent and child class.

class company:
    def __init__(self):
        self._companyname="Google"
    
class branch(company):
    pass

c1=company()
print(c1._companyname)      # o/p: Google
b1=branch()
print(b1._companyname)      # o/p: Google
