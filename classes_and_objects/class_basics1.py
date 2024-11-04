# Imagine that we have 100 cars. Instead of creating 100 variables and functions/methods for each car.
# We can create a class with all properties and function for cars.

class vehicle:
    
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def moves(self):
        print(f"moves along.......🚘🚔🚑🚎🏎️🏍️🛵🚲🛴")

    def get_make_model(self):
        print(f"I'm a {self.name} {self.model}.")


my_car=vehicle("Tesla", "Model Y")

my_car.moves()                                  # o/p: moves along.......🚘🚔🚑🚎🏎️🏍️🛵🚲🛴
my_car.get_make_model()                         # o/p: I'm a Tesla Model Y.

your_car=vehicle("maruti", "500")

your_car.moves()                                # o/p: moves along.......🚘🚔🚑🚎🏎️🏍️🛵🚲🛴
your_car.get_make_model()                       # o/p: I'm a maruti 500.