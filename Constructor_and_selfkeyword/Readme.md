Constructor and Self Keyword Learing Order:

1. constructor_basics.py


Note:

what is constructor?

A constructor is a unique function/method that gets called automatically when a object is created of a class.

For Ex:

1. Let's say we have a class college. Inside the college we have few functions like def mech(self), def civil(self) those method we need to call from objects.
2. Like we need to create an object like student1 = college() then  student1.mech() (or) student1.civil() so that the object can access the methods inside the class.
3. But if we have def __init__ (self) method created inside a class then this method will be automatically called while creating the object.
4. If i create a object  student2 = college () then  def __init__(self) will be automatically called by the student2 object.


class college:
   
   def __init__(self):
      print ("Please show your ID Card 🧑‍🎓👨‍🎓")

   def mech(self):
      print ("I am from mech dept")

   def civil(self):
      print ("I am from civil dept")
    
student1 = college()             # o/p:  Please show your ID Card 🧑‍🎓👨‍🎓
student1.mech()                  # o/p:  I am from mech dept     

student2 = college()             # o/p:  Please show your ID Card 🧑‍🎓👨‍🎓
student2.civil()                 # o/p:  I am from civil dept









