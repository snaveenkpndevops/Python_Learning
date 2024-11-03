a=[10,11,12,13]

# This will print the first index value
print(a[1])    # o/p: 11

# This will print the zero index value
print(a[0])    # o/p: 10

# Insert 20 in index 0
a.insert(0, 20)
print(a)       # o/p: [20, 10, 11, 12, 13]

# Insert 30 in index 0 (another method)
a[0]=30
print(a)       # o/p: [30, 10, 11, 12, 13]

# Remove index 4 value
a.pop(4)
print(a)       # o/p: [30, 10, 11, 12]

# Remove the last value of the list
a.pop()
print(a)       # o/p: [30, 10, 11]


# Join a and b value in list a
b=["jaddu", "pandya", "pant"]
a.extend(b)
print(a)       # o/p: [30, 10, 11, 'jaddu', 'pandya', 'pant']