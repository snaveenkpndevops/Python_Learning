# Now this will print 0 1 2 3 4 and then i value will become 5
# which is equals the while condition so the while condition becomes false
i=0
while(i<5):
    print (i)
    i=i+1


# Write a program to print first 10 natural numbers in reverse order.
i=10
while (i>0):
    print (i, end=",")
    i=i-1

# Write a program to find the factorial of a number.
print()
number=int(input("Please Enter the number:  "))
num=number
count=1
while(num>0):
    count=count*num
    num=num-1

print(f"The factorial of {number} is {count}")