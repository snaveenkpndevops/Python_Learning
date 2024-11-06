## Constructor and Self Keyword Learing Order:

1. Types_of_classvariable.py
2. 


### Note:

## Types of class variable ?

1. Instance Variable
2. Class Variable

### Example for class variable:

Note: 

1. The variables that is inside constructor def __init__() is consider as instance variable.vars

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

## Types of class methods ?

1. Instance method
2. Class method
3. static method













