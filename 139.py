users = {}
while True:
    print("1:Sign In\n2:Log In\n3:Exit")
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        password1 = input("Enter your password: ")
        password2 = input("Confirm password: ")
        if password1 == password2:print("Successfully Logined")
        else:
            print("Passwords doesn't match")
            password2 = input("Confirm password")
        users[name] = password1
        print(users)
    elif choice == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if name in users and users[name] == password:print("Login successful!")
        else:print("Invalid username or password.")
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    else:print("Invalid choice.")