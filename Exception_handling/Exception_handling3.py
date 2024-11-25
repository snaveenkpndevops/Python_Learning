# Exception handling using try, except, finally.
# If we pass string in variable then it will throw exception. So it will print some error occured.
# finally -->  If the Input is correct or not. we will get the finally result.

try:
    a=int(input("Enter the number: "))      # I/P: 20
    b=int(input("Enter the number: "))      # I/P: hi

except ValueError as e:
    print ("ValueError", e)                 # O/P: ValueError invalid literal for int() with base 10: 'hi'                   

except Exception:
    print ("Something Wrong")              


finally:
    print ("Done")                          # O/P: Done





