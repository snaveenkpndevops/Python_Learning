# parameterized functions/methods --> we will be passing the input to methods while calling the methods

def painter(msg):
    print (f"Message: {msg}")

painter("paint my house")


# Ex: 1 --> Find Odd or even using parameterized methods

def odd_or_even(number):
    if (number%2==0):
        print (f"The number {number} is even")
    else:
        print (f"The number {number} is odd")

a=int(input("Please Enter the number you want to check:  "))    

odd_or_even(a)


# Ex: 2 --> Find pass or fail using parameterized methods

def pass_or_fail (marks):
    if (marks>35 and marks<75):
        print (f"You pass the exam but need to work hard 🤓🥲 🙂")
    elif (marks>75):
        print (f"Good!!! you are an outstanding student 😎👌😊")
    else:
        print (f"olunga padida parama 😤😢😰😩🤬")

mark=int(input("Please enter your mark: "))
pass_or_fail(mark)


# Ex: 3 --> Add 2 numbers using parameterized methods

def add (num1, num2):
    print(f"The addition of {num1} and {num2} is {num1+num2}")
    

c=int(input("Please enter the first number: "))
d=int(input("Please enter the second number: "))
add(c,d)