#use for loop with list
a=[1,2,3,4,5,6]
for i in a:
    print (i)

#Write a program to read 5 numbers from the keyboard and find their sum and average
a=[]
count=0
for i in range (5):
    num=int(input("Please enter number {i}: "))
    a.append(num)
    count=count+1

sum=0
for i in a:
  sum=sum+i


print (f"The sum is {sum}")
print (f"The average is {sum/count}")


