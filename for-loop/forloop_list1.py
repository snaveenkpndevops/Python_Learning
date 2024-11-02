#Write a program to display the cube of the number up to an integer
a=[]
for i in range (5):
    num=int(input("Please enter number {i}: "))
    b=num*num*num
    a.append(b)

print (f"{a}")
