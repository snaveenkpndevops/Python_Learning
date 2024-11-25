# Exception handling using try, except.
# If we pass string in variable then it will throw exception. So it will print some error occured.

try:
    a=int(input("Enter the number: "))      # I/P: 20
    b=int(input("Enter the number: "))      # I/P: 10
    c=input("Enter the word: ")             # I/p: hi

    print(d)

except ValueError as e:
    print ("ValueError", e)                             

except TypeError as e:
    print ("TypeError", e)          

except Exception:
    print ("Something Wrong")              # O/P: Something Wrong





