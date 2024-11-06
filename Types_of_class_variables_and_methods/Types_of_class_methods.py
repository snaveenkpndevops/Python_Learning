# Fuction are also called as methods.

# Types of class methods

# 1. Instance method     2. class method      3. static method


class college:
    college_name = "OXFORD UNIVERSITY 🏫🏫"
    place = "UK"

    # Constructor
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    # This is Instance method [mostly used], It will change based on the object.
    def display(self):
        print (f"My name is {self.name}, am from {self.dept} department {self.college_name} {self.place}")

    # This is class method, which is rarely used. It will be same with different object.
    @classmethod
    def change_collegename(cls):
        cls.college_name = "Veltech Multitech Engineering College"
        print (f"College name change to {cls.college_name}")
    
    # This is static method [If we want a method (or) function that doesn't use class method or instance method. In this case we will use this method. ]
    @staticmethod
    def info():
        print(f"100% placement quarentee!!!")


student1=college("naveen", "mech")
student2=college("jackie", "Aero")
student3=college("angelina", "english_literature")

student1.display()    # o/p: My name is naveen, am from mech department OXFORD UNIVERSITY 🏫🏫 UK
student2.display()    # o/p: My name is jackie, am from Aero department OXFORD UNIVERSITY 🏫🏫 UK
student3.display()    # o/p: My name is angelina, am from english_literature department OXFORD UNIVERSITY 🏫🏫 UK

college.change_collegename()    # o/p:  College name change to Veltech Multitech Engineering College
student1.info()                 # o/p:  100% placement quarentee!!!


# Note:

# In the above code:

# 1. def display()  -->  It is a instance method, It will change based on the object. [We mostly use this method.]

# 2.  @classmethod
#     def change_collegename(cls):          -->  This is class method, which is rarely used. It will be same with different object.

# 3. @staticmethod
#     def info():                                           --> This is static method [If we want a method (or) function that doesn't 
#         print(f"100% placement quarentee!!!")             -->   use class method or instance method. In this case we will use this method. ]
