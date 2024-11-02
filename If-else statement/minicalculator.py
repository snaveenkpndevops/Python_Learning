#Make a mini calaculator
#Get input for 2 numbers a and b
#Get input from user whether to add/sub/mul/div
#based on the user input we need to perform the operation.

a= int(input("Please enter the first number : "))
b= int(input("Please enter the second number : "))
operation= input("Enter the Operation to be performed: ")

if (operation=="add"):
    print (f"The adddition of a and b is {a+b}")
elif (operation=="sub"):
    print (f"The subtraction of a and b is {a-b}")
elif (operation=="mul"):
    print (f"The muliply of a and b is {a*b}")
elif (operation=="div"):
    print (f"The adddition of a and b is {a/b}")
else:
    print ("Please enter a valid operator")