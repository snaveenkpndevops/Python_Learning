Exception_handling learning Order:

1. Exception_handling.py
2. Exception_handling1.py
3. Exception_handling2.py
4. Exception_handling3.py


## Note:

### What is Exception_handling?

There are 3 types of error:

1. Compile Time Error:

    Python editor will read each and every line of the code. If there are any error in code such as in name, semicolon, bracket. This will cause an error. This is called `compile time error` (syntax error).

    ```
    // Example: 

    print("Hi")                 # O/P: Hi

    print ("Bye")               # O/P: Bye

    printtt ("Hello")           # O/P: Nameerror [Print spelling mistake]

    ```


2. Logical Error:

    Instead of adding (a+b) we're adding (a+a). so here we will get the output without any error message. But we're doing logical error.

    ```
    // Example: 

    a=10
    b=20

    print (a+a)               # O/P: 20

    ```

3. Runtime Error:

    Error occur in the middle of the program running (Runtime).This is called Runtime Error.

    ```
    // Example: 

    a=int(input("Enter the number: ))        # I/P: 10

    b=int(input("Enter the number: ))        # I/P: Hi

    print (a+b)                              # O/P: ValueError --> Invalid Literal for int() with bas10:'Hi'                         

    ```

## Note:

1. The First two error is occured by developer. we have to be aware while writting the code.
2. The 3rd error, that is `runtime error`. Developers as well as user should be aware. so for this error we can use `Exceptional Handling` to handle this error.

