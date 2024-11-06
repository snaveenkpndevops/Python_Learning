## Constructor and Self Keyword Learing Order:

1. Types_of_classvariable.py
2. 


### Note:

## Types of class variable ?

1. Instance Variable
2. Class Variable

### Example for class variable:

Note: 

### 1. Instance Variable:

The variables that is inside constructor `def __init__()` is consider as instance variable.

for ex: 

    ```python
    class college:
        college_name = "OXFORD UNIVERSITY 🏫🏫"
        place = "UK"

        def __init__(self, name, dept):
            self.name = name
            self.dept = dept

        def display(self):
            print (f"My name is {self.name}, am from {self.dept} department {self.college_name} {self.place}")


    student1=college("naveen", "mech")
    student2=college("jackie", "Aero")
    student3=college("angelina", "english_literature")

    student1.display()    # o/p: My name is naveen, am from mech department OXFORD UNIVERSITY 🏫🏫 UK
    student2.display()    # o/p: My name is jackie, am from Aero department OXFORD UNIVERSITY 🏫🏫 UK
    student3.display()    # o/p: My name is angelina, am from english_literature department OXFORD UNIVERSITY 🏫🏫 UK


Note: 

1. The variables that is inside `constructor def __init__()` is consider as `instance variable`.

for ex:

    ```python
    def __init__(self, name, dept):
            self.name = name
            self.dept = dept

Here `self.name, self.dept` is a `instance variable`. `self refers to student1, student2, student3`. The value of the 
variable will get changed for every object like for student1 we have different value for each variable.
That's why it is called Instance variable.

### 2.  Class Variable:

Variable that is inside class and not inside the constructor `def __init__` is consider as `class variable`.

for ex:

    ```python
    class college:
        college_name = "OXFORD UNIVERSITY 🏫🏫"
        place = "UK"

Here `college_name` and `place` --> This variable that doesn't change even the object change (student1, student2, student3) is called `class variable`.
Here student1 can have diff name, dept and student2 can have diff name and dept but they are in same college.
college and place variable will not change.

### Overall:

1. `Changing variable` should be define in `Instance Variable`.
2. `Variable that doesn't change` should be consider as `class variable`.

## Types of class methods:

1. Instance method
2. Class method
3. static method

for Ex:

    ```python

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


Note:

In the above code:

1. def display()  -->  It is a instance method, It will change based on the object.

2.  @classmethod

    def change_collegename(cls):          -->  This is class method, which is rarely used. It will be same with different object.

3. @staticmethod

    def info():        
        print(f"100% placement quarentee!!!")     --> This is static method [If we want a method (or) function that doesn't use class method or instance method. In this case we will use this method. ]       












