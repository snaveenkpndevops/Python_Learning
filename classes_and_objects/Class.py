# Create a Class named Goa and create 2 variable --> "name", "drinks" 
# And 2 methods  --> "party", "beach"

class goa():
    name="abcde"
    drinks="yes"

    def party(self):
        print ("lets party 🍕🍔🍟🍾🍻🍺🥂")

    def beach(self):
        print("Enjoying the beach 🏖️⛱️🌄🏔️⛰️🗻")


# Now ramesh and suresh can enter goa class
ramesh=goa()
suresh=goa()

# In goa class we have a configured a default name if ramesh and suresh
# doesn't have a name, it will set the default name that is abcde to ramesh and suresh
print (f"The default ramesh name in goa is {ramesh.name}")  # o/p: The default ramesh name in goa is abcde
print (f"The default ramesh name in goa is {suresh.name}")  # o/p: The default suresh name in goa is abcde


# Now we configuring name to ramesh and suresh using name variable
ramesh.name="Ramu"
suresh.name="Somu"

# Now the Output of Ramesh and suresh name will be Ramu and Somu
print (f"Now the ramesh name in goa is {ramesh.name}")      # o/p: Now the ramesh name in goa is Ramu
print (f"Now the suresh name in goa is {suresh.name}")      # o/p: Now the suresh name in goa is Somu


# Now we are trying to access the methods inside the goa class
ramesh.party()                                              # o/p: lets party 🍕🍔🍟🍾🍻🍺🥂
suresh.beach()                                              # o/p: Enjoying the beach 🏖️⛱️🌄🏔️⛰️🗻