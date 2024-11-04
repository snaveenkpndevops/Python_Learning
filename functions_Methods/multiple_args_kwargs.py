def func(a, b, *args, option=False, **kwargs):

    print("")                            # o/p: 
    print(a,b)                           # o/p: 1 3
    print(args)                          # o/p: (10, 20)
    print(option)                        # o/p: False
    print(kwargs)                        # o/p: {'name': 'Tom', 'Salary': 50000}


func (1,3,10,20,name="Tom",Salary=50000)