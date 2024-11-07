# Inheritance_and_its_types Learing Order:

1. Single_Inheritance.py
2. return_ex1.py
3. return_ex2.py


## Note:

### Inheritance Concept:

1. Father Property to his son.
2. Son can access his Father property.

### Types of inheritance:

1. Single Inheritance
2. Multiple Inheritance
3. multi-level Inheritance
4. hierarchical inheritance
5. Hybrid Inheritance


### 1. Single Inheritance:

 Here is an Single Inheritance image:

![Example Image](Images/Single_Inheritance.png)   

    ```python
    # Single Inheritance
    # Let's consider there is a father and a son. Here son has all rights to use the father wealth (money, car, home, business etc.)

    class father():

        def money(self):
            print ("Dad's money....")

        def car(self):
            print ("Dad's Car....")

    # Here Son class inherits from the father class 
    class son(father):

        def bike(self):
            print ("son's bike")


    jackie=son()
    jackie.money()    # o/p:  Dad's money....
    jackie.car()      # o/p:  Dad's Car....
    jackie.bike()     # o/p:  son's bike
    ```
### 2. Multiple Inheritance
### 3. multi-level Inheritance
### 4. hierarchical inheritance
### 5. Hybrid Inheritance







