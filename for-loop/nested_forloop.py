# *
# **
# ***
# ****
# *****    Create a right angle triangle pattern using nested for loop

for i in range(5):
    print ()
    for j in range(5):
        if (j<=i):
            print ("*", end=" ")


# *****
# ****
# ***
# **
# *  Create a reverse right angle triangle pattern using nested for loop

for i in range(5):
    print ()
    for j in range(5):
        if (j>=i):
            print ("*", end=" ")

# *****
# *****
# *****
# *****
# *****  Create a rectangle pattern using nested for loop

for i in range(5):
    print ()
    for j in range(5):
        print ("*", end=" ")

#     *
#    ***
#   *****
#  *******
# *********    Create a triangle pattern using nested for loop


print()
# Number of rows for the triangle
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line
    print()

            
