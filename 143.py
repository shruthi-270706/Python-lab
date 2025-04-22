phone_numbers = {}  
while True:
    print("\n1:Add\n2:Update\n3:Delete\n4:Search\n5:View Details\n6:Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:  
        name = input("Enter name: ")
        if name in phone_numbers:print(f"{name} is already in records")
        else:
            p_number = int(input(f"Enter {name}'s phone number: "))
            phone_numbers[name] = p_number  
            print(f"{name} is added with phone number: {p_number}")
    elif choice == 2:  
        name = input("Enter name to update phone number: ")
        if name in phone_numbers:
            p_number = int(input(f"Enter {name}'s updated phone number: "))
            phone_numbers[name] = p_number  
            print(f"{name}'s phone number updated to: {p_number}")
        else:print(f"{name} is not present in records")
    elif choice == 3: 
        name = input("Enter name to delete: ")
        if name in phone_numbers:
            del phone_numbers[name]  
            print(f"{name} has been removed from records.")
        else:print(f"{name} is not present in records")
    elif choice == 4:  
        name = input("Enter name to search: ")
        if name in phone_numbers:print(f"{name}'s phone number: {phone_numbers[name]}")
        else:print(f"{name} is not present in records")
    elif choice == 5: 
        if phone_numbers:
            for name, p_number in phone_numbers.items(): 
                print(f"{name}: {p_number}")
        else:print("No records found.")
    elif choice == 6:
        print("Exiting program. Goodbye!")
        break
    else: print("Invalid input. Please enter a valid choice.")