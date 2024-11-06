# This is another method of constructor_purpose1.py, we are passing the input for each variable using object.variable = value.

class college:
    
    def __init__(self):
        self.name = ""
        self.dept = ""
        self.job  = ""
        self.emoji= ""

    def profession (self):
        print (f"My name is {self.name} am from {self.dept} department, I will become {self.job}  {self.emoji} ")


student1=college()
student1.name="naveen"
student1.dept="mech"
student1.job="automobile_designer"
student1.emoji="🚓🚗🏎️✈️🚲🚉🚅🚂"

student2=college()
student2.name="dhoni"
student2.dept="cricket"
student2.job="cricketer"
student2.emoji="🏏⚽🤾‍♀️🤾‍♂️🏅🏐🏏🏏"


student1.profession()     #o/p:  My name is naveen am from mech department, I will become automobile_designer  🚓🚗🏎️✈️🚲🚉🚅🚂 
student2.profession()     #o/p:  My name is dhoni am from cricket department, I will become cricketer  🏏⚽🤾‍♀️🤾‍♂️🏅🏐🏏🏏
