import hashlib

def encrypt(text):
    return hashlib.sha256(text.encode()).hexdigest()

def add_password():
    site = input("Website: ")
    user = input("Username: ")
    pwd = input("Password: ")
    encrypted_pwd = encrypt(pwd)

    with open("passwords.txt", "a") as f:
        f.write(f"{site} | {user} | {encrypted_pwd}\n")

    print("Password saved!")

def view_passwords():
    try:
        with open("passwords.txt", "r") as f:
            print("\n--- Saved Passwords ---")
            print(f.read())
    except FileNotFoundError:
        print("No passwords saved yet!")

while True:
    print("\n1. Add New Password")
    print("2. View Saved Passwords")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
