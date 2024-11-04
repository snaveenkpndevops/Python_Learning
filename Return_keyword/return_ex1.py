# get username and pwd from user and if they match
# send true else false

username="naveen"
password=12345

uname=input("Please enter your username: ")
pwd=int(input("Please enter your password: "))

def validate(uname, pwd):
    if (username==uname and password==pwd):
        return True
    else:
        return False

result=validate(uname, pwd)
print(result)