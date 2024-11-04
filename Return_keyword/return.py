# Return
# Return is a something that just return some value to the variable while the function executes.
# So here we are calling the painter function using msg variable and in return we are getting value "I am painter"
# Which is stored as a value in msg variable

def painter():
    return "I am painter"

msg=painter()  # This will just call the function.  o/p: no output

print(msg)  # This will also call the function and print the result.  o/p: I am painter