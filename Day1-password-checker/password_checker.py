password = input("enter password :")

if len(password) < 6:
    print("weak password ")

elif len(password) <10 :
    print("medium password")
    
else:
    print("strong password")

if any(char.isdigit() for char in password):
    print("there are didgit in this ")

if any(char.isupper() for char in password):
    print("passowrd is in upper case ")

if any(char in "@#$%&" for char in password):
    print("password has special charcter")