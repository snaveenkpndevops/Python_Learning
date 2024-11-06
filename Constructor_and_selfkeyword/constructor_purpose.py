# The main purpose of a constructor is to initialize or assign values to the data members of that class.
# It sets up the initial state of the object.

class college:
    
    def __init__(self, name, dept, job, emoji):
        self.name = name
        self.dept = dept
        self.job  = job
        self.emoji=emoji

    def profession (self):
        print (f"My name is {self.name} am from {self.dept} department, I will become {self.job}  {self.emoji} ")


student1=college("naveen","mech","automobile_designer", "🚓🚗🏎️✈️🚲🚉🚅🚂")
student2=college("dhoni","cricket","cricketer", "🏏⚽🤾‍♀️🤾‍♂️🏅🏐🏏🏏")
student3=college("jackie_chan","acting","actor", "🧑‍🎤👨‍🎤🎭🥷🥋🥋")
student4=college("Tata", "business", "business_man", "🧑‍💼👨‍💼👩‍💼🏗️🏢🏦🏨🏫🏭")


student1.profession()     #o/p:  My name is naveen am from mech department, I will become automobile_designer  🚓🚗🏎️✈️🚲🚉🚅🚂 
student2.profession()     #o/p:  My name is dhoni am from cricket department, I will become cricketer  🏏⚽🤾‍♀️🤾‍♂️🏅🏐🏏🏏
student3.profession()     #o/p:  My name is jackie_chan am from acting department, I will become actor  🧑‍🎤👨‍🎤🎭🥷🥋🥋
student4.profession()     #o/p:  My name is Tata am from business department, I will become business_man  🧑‍💼👨‍💼👩‍💼🏗️🏢🏦🏨🏫🏭