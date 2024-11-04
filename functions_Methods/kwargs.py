# Keyword with arguments
# Here we are going to pass key and value as a argument in function/methods.
## Here ** represent key and value (dictionary value)

def mult_named_items(**kwargs):
    print(kwargs)                       # o/p: {'f_name': 'naveen', 'l_name': 'srinivasan'}
    print(type(kwargs))                 # o/p: <class 'dict'>


mult_named_items(f_name="naveen", l_name="srinivasan")     