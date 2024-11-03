# Dictionary

# 1. Dictionary will not allow duplicate. It will overwrite the existing value.
# 2. It is also called key-value pair.

a={"name": "naveen",
   "age": 25,
   "dept": "mech"}

print(a)  # o/p:  {'name': 'naveen', 'age': 25, 'dept': 'mech'}

print(a["name"])  # o/p:  naveen


# 3. we can store list, tuple and set inside dictionary

b={"name": ["naveen", "Srinivasan"],
   "age": (25, 30)
   }

print(b)   # o/p:  {'name': ['naveen', 'Srinivasan'], 'age': (25, 30)}


# Only keys will get print
print (b.keys())   # o/p:  dict_keys(['name', 'age'])

# Only values will get print
print (b.values())   # o/p:   dict_values([['naveen', 'Srinivasan'], (25, 30)])


# 4. we can able to modify the value of dictionary

b["name"]=["ms", "dhoni"]
print(b)     # o/p:  {'name': ['ms', 'dhoni'], 'age': (25, 30)}