#Get input from user if it greater than 70. Get their names, age and print eligible
score=int(input("Please Enter your score: "))

if (score>=70):
    name=input("Please Enter your name: ")
    age=int(input("Please Enter your age: "))
    if (age>18 and age<24):
        print (f"{name} is eligible for education loan")
    else:
        print (f"Oh Sorry {name} you're age does not comes under eligible category")
else:
    print ("Oh Sorry!!! You are not eligible for education loan")