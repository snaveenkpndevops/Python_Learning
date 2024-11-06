## Constructor and Self Keyword Learing Order:

1. constructor_basics.py
2. constructor_purpose.py
3. constructor_purpose1.py
4. empty_class.py


### Note:

what is constructor?

A constructor is a unique function/method that gets called automatically when a object is created of a class.

For Ex:

1. Let's say we have a class college. Inside the college we have few functions like def mech(self), def civil(self) those method we need to call from objects.
2. Like we need to create an object like student1 = college() then  student1.mech() (or) student1.civil() so that the object can access the methods inside the class.
3. But if we have def __init__ (self) method created inside a class then this method will be automatically called while creating the object.
4. If i create a object  student2 = college () then  def __init__(self) will be automatically called by the student2 object.


## College Class Example

This Python script demonstrates a simple `College` class with an initializer and methods representing different departments.

### Code

    ```python
    class college:
    
    def __init__(self):
        print ("Please show your ID Card 🧑‍🎓👨‍🎓")

    def mech(self):
        print ("I am from mech dept")

    def civil(self):
        print ("I am from civil dept")
        
    # Creating instances of the College class
    student1 = college()             # Output: Please show your ID Card 🧑‍🎓👨‍🎓
    student1.mech()                  # Output: I am from mech dept     

    student2 = college()             # Output: Please show your ID Card 🧑‍🎓👨‍🎓
    student2.civil()                 # Output: I am from civil dept


### Purpose:

1. The main purpose of a constructor is to initialize or assign values to the data members of that class.
2. It sets up the initial state of the object.


### Constructor Definition:

In Python, a constructor is a special method used to initialize an object of a class. The constructor method in Python is called `__init__`. It is automatically invoked when an instance (object) of a class is created.

* The constructor method is defined using the `def` keyword followed by `__init__`.
* It always takes at least one argument, `self`, which refers to the instance being created.











