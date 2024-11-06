class fruit:
    
    def __init__(self,color):
        self.color=color

apple=fruit("red")
print(apple.color)      # o/p:  red


# Note:

# 1. In def __init__()  if we remove self from () then we will face error.
# 2. What this self will do? 

# when we create a object like apple=fruit("red"), this apple will pass to the class.
# and inside def __init__(apple, color)  it will replace self word and change to the object that is apple. 