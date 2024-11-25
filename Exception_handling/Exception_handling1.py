# Exception handling using try, except.
# If we pass string in variable then it will throw exception. So it will print some error occured.

try:
    a=int(input("Enter the number: "))      # I/P: 2
    b=int(input("Enter the number: "))      # I/P: f

    print(a+b)

except Exception as e:
    print (e)                               # O/P: invalid literal for int() with base 10: 'f'


#-------------------------------#

try:
    a=input("Enter the word: ")      # I/P: Hi
    b=input("Enter the word: ")      # I/P: Bye

    print(a/b)

except Exception as e:
    print (e)                               # O/P: unsupported operand type(s) for /: 'str' and 'str'


# Note:

# 1. ValueError -->   In String Variable we gave input as integer, in integer variable we gave input as string.

# 2. TypeError  -->   Operand String divided by int.

# 3. NameError  -->  print variable d. but we don't have a variable d defined in our code.


