# Set

a={10,11,12,13,14,10}

# 1. Duplicate Value is not accepted
print(a)    # o/p: {10, 11, 12, 13, 14}

# 2. We cannot modify the sets
# a[0]=20
# print(a)  # o/p: error

# 3. We can add/update/remove value from sets
a.add(19)
a.remove(14)
print(a)  # o/p: {19, 10, 11, 12, 13}

# 4. The Order of the value will be changed everytime when we run the code.
