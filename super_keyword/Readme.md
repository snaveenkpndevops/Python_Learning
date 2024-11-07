Super Keyword learning Order:

1. super_keyword.py
2. super_keyword_1.py


Note:

### when to use super Keyword?

Let's consider we have a father class and son class. Both father and son having constructor `def __init__()`. When we create a object for son class.
It will only call the constructor of son class. It will not call the constructor of father class.
If son class doesn't have constructor `def __init__()` then it will call the constructor of father class.

for example:

    ```
    python
    class father():

        def __init__(self):
            print ("father name is lee....")
        
        def money(self):
            print ("father's money...")

    class son(father):

        def __init__(self):
            print ("son name is jackie....")
        
        def bike(self):
            print ("son's bike...")


    jackie=son()      #  o/p:  son name is jackie....
    jackie.money()    #  o/p:  father's money...
    jackie.bike()     #  o/p:  son's bike...

    ```


But If i want both father and son constructor to be called while creating the object for son class. In this case we will use super keyword.

    ```
    class father():

        def __init__(self):
            print ("father name is lee....")
        
        def money(self):
            print ("father's money...")

    class son(father):

        def __init__(self):
            # super keyword  -->  This will inherit the parent constructor also
            super().__init__()
            print ("son name is jackie....")
        
        def bike(self):
            print ("son's bike...")


    jackie=son()      #  o/p:  father name is lee....
                    #  o/p:  son name is jackie....

    jackie.money()    #  o/p:  father's money...
    jackie.bike()     #  o/p:  son's bike...

    ```
