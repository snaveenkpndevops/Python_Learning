# Ex1: Get user input for 2 numbers and print the number b/w a and b
a=int(input("Please Enter the first number: "))
b=int(input("Please Enter the Second number: "))
for i in range(a,b):
    print (i)

# Ex1: Get user input for 2 numbers and print the even number b/w a and b
a=int(input("Please Enter the first number: "))
b=int(input("Please Enter the Second number: "))
for i in range(a,b):
    if (i%2==0):
      print (i)