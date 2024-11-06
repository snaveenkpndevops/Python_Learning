# what is constructor?

# A constructor is a unique function/method that gets called automatically when a object is created of a class.

# For Ex:

# 1. Let's say we have a class college. Inside the college we have few functions like def mech(self), def civil(self) those method we need to call from objects.
# 2. Inside college class we have one more method that is def __init__(self) which is called as constructor. This will be called automatically while creating the object.
# 3. Like in the below example, I created student1 object -->   student1 = college()   -->  while creating the object student1 it will automaticallyu call the constructor that is def__init__(self).

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
