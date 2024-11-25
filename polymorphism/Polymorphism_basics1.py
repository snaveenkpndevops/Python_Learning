# Polymorphism

# The word polymorphism means having many forms.

# Here the result will get changed based on object we called. If we call India.capital() it will show india class capital method.

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

# O/P:

# New Delhi is the capital of India.
# Hindi is the most widely spoken language of India.
# India is a developing country.
# Washington, D.C. is the capital of USA.
# English is the primary language of USA.
# USA is a developed country.