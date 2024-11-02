# ex1: If True then print yes else print no o/p: yes
if (True):
    print ("yes")
else:
    print ("No")

# ex2: If RCB wins print ee sala cup namde else Better luck next time
rcb=input("Enter the result of ipl: ")

if (rcb.lower()=="wins"):
    print ("ee sala cup namde")
else:
    print ("Better luck next time")


#  ex3: If marks greater than 35 then pass, else fail
marks=int(input("Please Enter Your Mark: "))
if(marks>=35):
    print ("Congrats!!! you pass the exam 👌😎")
else:
    print ("Olunga padida parama 😒🥺😒")

#  ex4: Get a number from user and check whether the number is divisible both by 3 and 5
num=int(input("Please Enter the number: "))
if ((num%3==0) and (num%5==0)):
    print ("The number is divisible by both 3 and 5")
else:
    print ("The number is not divisible by both 3 and 5")


#  ex5: Check the number is odd or even
num=int(input("Please enter the number: "))
if ((num%2==0)):
    print (f"The num {num} is even")
else:
    print (f"The num {num} is not even")

#  ex6: If marks greater than 35 then pass, less than 35 fail, inbetween 35 to 70 average
marks=int(input("Please Enter Your Mark: "))
if(marks>75):
    print ("Congrats!!! you are topper 👌😎")
elif(marks>35 and marks<75):
    print ("Dei nee yeppadiyo pass panita 😁")
else:
    print ("Olunga padida parama 😒🥺😒")