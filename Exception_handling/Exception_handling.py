# Exception handling using try, except.
# If we pass string in variable then it will throw exception. So it will print some error occured.

try:
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))

    print(a+b)

except Exception:
    print ("some error occured")