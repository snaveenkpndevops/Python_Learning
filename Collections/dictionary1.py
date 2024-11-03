# Dictionary

a={"name": "naveen",
   "age": 25,
   "dept": "mech"}

print (a)  # o/p:  {'name': 'naveen', 'age': 25, 'dept': 'mech'}

# Add job field in dictionary
a["job"]="IT"
print (a)  # o/p: {'name': 'naveen', 'age': 25, 'dept': 'mech', 'job': 'IT'}


# update age in dictionary
a.update({"age": 26})
print (a)  # o/p: {'name': 'naveen', 'age': 26, 'dept': 'mech', 'job': 'IT'}

# delete job in dictionary
a.pop("job")
print (a)  # o/p: {'name': 'naveen', 'age': 26, 'dept': 'mech'}

# delete dept in dictionary (another method)
del a["dept"]
print (a)  # o/p: {'name': 'naveen', 'age': 26}


# Clear all values from dictionary.
a.clear()
print (a)  # o/p: {}