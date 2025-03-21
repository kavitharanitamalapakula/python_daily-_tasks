# Generate a Random Password
import random
import string
def generate_password(length=6):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password

# Login System with Limited Attempts
def passwords(user_created_password):
    attemps = 3
    while attemps>0:
        password_check = input("Enter Passsword for Login : ")
        if password_check == user_created_password:
            print("login success")
            break
        attemps-=1
        if attemps==0:
            print("please try again Later! your attemps are exceeded🚫")
        else:
            print(f"Login faild ! you have {attemps} more Attemps")
    
# Verify the Generated Password
password = generate_password()
print("Your generated password is:", password)
userPssword = input("Enter generated password : ")
while True:
    if password == userPssword:
        print("Verification Done")
        user_created_password = input("Create new password : ")
        print("created successfully")
        passwords(user_created_password)
        break
    else:
        print("Please try again")
        break
