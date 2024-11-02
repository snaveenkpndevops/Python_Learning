#Count the number of odd and even numbers b/w the a and b
a=int(input("Please Enter the first number: "))
b=int(input("Please Enter the Second number: "))
odd_count=0
even_count=0
for i in range(a,b):
    if(i%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1

print(f"The even count is {even_count}")
print(f"The odd count is {odd_count}")
