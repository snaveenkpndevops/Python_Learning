# Public Variable

# self.companyname="Google" is a public variable. 
# why because for private we will use self.__companyname and for protected variable we will use self._companyname.

# In this public variable anyone can change the value of companyname using c1 object. 
# but we don't anyone to access or change the companyname variable that is inside class company. so for that we can use access modifier.
# It can be accessed by any class and object.

class company:
    def __init__(self):
        self.companyname="Google"

c1=company()
c1.companyname="Gooooooogle"
print(c1.companyname)     # o/p: Gooooooogle