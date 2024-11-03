# List

a=[1,2,3,4,5]
print (type(a))  #o/p:  <class 'list'>

print(a)  # o/p: [1,2,3,4,5]



# 1. Append will add the value at the end of the list.
a.append(6)  
print(a)    # o/p: [1,2,3,4,5,6]

# 2. In List, we can add all type of data types (int, string, boolean) etc.
a.append("dhoni")  
print(a)    # o/p: [1, 2, 3, 4, 5, 6, 'dhoni']

# 3. Duplicate Value is accepted
a.append(6)  
print(a)    # o/p: [1, 2, 3, 4, 5, 6, 'dhoni', 6]