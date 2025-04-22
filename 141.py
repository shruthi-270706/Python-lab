inventory = set()
sold_out = set()
while True:
    print("1.Add Item\n2.Remove Item\n3.Check if Item is in Stock")
    print("4.Mark Item as Sold Out\n5.Display Current Stock\n6.Display Sold-Out Items\n7.Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        item = input("Enter the unique ID of the item to add: ")
        if item in inventory:print(f"Item {item} is already in the inventory.")
        else:
            inventory.add(item)
            print(f"Item {item} added to the inventory.")
    elif choice == "2":
        item = input("Enter the unique ID of the item to remove: ")
        if item in inventory:
            inventory.remove(item)
            print(f"Item {item} removed from the inventory.")
        else:print(f"Item {item} is not in the inventory.")
    elif choice == "3":
        item = input("Enter the unique ID of the item to check: ")
        if item in inventory:print(f"Item {item} is available in stock.")
        else:print(f"Item {item} is not available in stock.")
    elif choice == "4":
        item = input("Enter the unique ID of the item to mark as sold out: ")
        if item in inventory:
            sold_out.add(item)
            inventory.remove(item)
            print(f"Item {item} marked as sold out.")
        else:print(f"Item {item} cannot be sold out as it is not in the inventory.")
    elif choice == "5":
        print("Current Stock:")
        for item in inventory:print(item)
    elif choice == "6":
        print("Sold-Out Items:")
        for item in sold_out:print(item)
    elif choice == "7":
        print("Exiting the system. Goodbye!")
        break