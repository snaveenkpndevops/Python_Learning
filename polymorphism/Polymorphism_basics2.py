# Polymorphism

# The word polymorphism means having many forms.

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

# Using polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Creating instances
dog = Dog()
cat = Cat()

# Passing different objects to the same function
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
