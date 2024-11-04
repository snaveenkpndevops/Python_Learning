# Applying Break and Continue in while loop

# o/p: for Continue
# The number is 9
# The number is 8
# The number is 7
# The number is 5
# The number is 4
# The number is 3
# The number is 2
# The number is 1

num=10

while(num>1):
    num=num-1
    if (num==6):
        continue
    print (f"The number is {num}")


# o/p: for Break
# The number is 9
# The number is 8
# The number is 7
   
num=10

while(num>1):
    num=num-1
    if (num==6):
        break
    print (f"The number is {num}")