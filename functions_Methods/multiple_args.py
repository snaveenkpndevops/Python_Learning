# Suppose we don't know how many arguments we will pass to functions.
# sometimes it may 2 or 3 or 20 etc. so how to handle this.

# Note: In def add (*num), The * represent that we can pass any number of args we want in methods/function. 

def add (*num):
    sum=0
    for i in num:
        sum=sum+i
    print(f"The sum is {sum}")

# o/p: The sum is 0
add()

# o/p: The sum is 5
add(5)

# o/p: The sum is 15
add(5,10)

# o/p: The sum is 60
add(10,20,30)