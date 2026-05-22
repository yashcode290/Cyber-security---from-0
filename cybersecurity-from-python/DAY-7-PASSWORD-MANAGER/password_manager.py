# ==========================================
# DAY 7 - PASSWORD MANAGER
# ==========================================

# File where passwords will be stored
FILE_NAME = "passwords.txt"


# ==========================================
# SAVE PASSWORD FUNCTION
# ==========================================

def save_password():

    website = input("Enter Website Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Format data
    data = f"Website: {website} | Username: {username} | Password: {password}\n"

    # Open file in append mode
    with open(FILE_NAME, "a") as file:
        file.write(data)

    print("\n✅ Password Saved Successfully!\n")


# ==========================================
# VIEW PASSWORDS FUNCTION
# ==========================================

def view_passwords():

    try:
        with open(FILE_NAME, "r") as file:

            print("\n===== SAVED PASSWORDS =====")

            for line in file:
                print(line)

    except FileNotFoundError:
        print("\nNo password file found.\n")


# ==========================================
# SEARCH PASSWORD FUNCTION
# ==========================================

def search_password():

    search = input("Enter Website Name to Search: ")

    try:
        with open(FILE_NAME, "r") as file:

            found = False

            for line in file:

                if search.lower() in line.lower():
                    print("\nPassword Found:")
                    print(line)
                    found = True

            if not found:
                print("\n❌ No matching website found.\n")

    except FileNotFoundError:
        print("\nNo password file found.\n")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("=================================")
    print("      PASSWORD MANAGER")
    print("=================================")

    print("1. Save Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Exit")

    choice = input("\nEnter Your Choice: ")

    # OPTION 1
    if choice == "1":
        save_password()

    # OPTION 2
    elif choice == "2":
        view_passwords()

    # OPTION 3
    elif choice == "3":
        search_password()

    # OPTION 4
    elif choice == "4":
        print("\nExiting Password Manager...")
        break

    else:
        print("\n❌ Invalid Choice\n")