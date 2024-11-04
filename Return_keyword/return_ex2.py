# Get input for a and b function called add() which should return the sum of a and b.
# And multiply thta sum with c.

def add(num1,num2):
    return num1+num2


a=int(input("Please Enter Number1: "))
b=int(input("Please Enter Number2: "))
c=int(input("Please Enter Number3: "))

maths=add(a,b)

result=maths*c

print(f"The result of (a+b)*c is {result}")