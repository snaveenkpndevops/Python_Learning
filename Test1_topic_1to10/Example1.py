# login validation of user using Bank Class

class Bank:
    # class variable
    bank_name = "Indian_Bank"
    account_balance = 10000

    #username and password list (collection)
    user_name_list = ["naveen", "dhoni", "jaddu"]
    password_list = ["naveen@123", "dhoni@123", "jaddu@123"]

    # constructor
    def __init__(self, user_name, account_id, password):
        # instance Variable
        self.uname = user_name
        self.acc_id = account_id
        self.pwd = password

    def validate(self):
        if self.uname in self.user_name_list:
            index=self.user_name_list.index(self.uname)
            if (self.pwd == self.password_list[index]):
                print (f"Validation success....")
                return True
            else:
                 print (f"Password Incorrect...")
                 return False
        else:
            print (f"Username not found...")
            return False
        

    # Instance method
    def login (self):
        login_status=Bank.validate(self)
        return login_status


            
client=Bank("naveen", "1234", "naveen@123")
result=client.login()
print (result)