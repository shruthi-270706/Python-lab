friends = {}
while True:
    print("\nOptions:")
    print("1. Send Friend Request\n2. Accept Friend Request\n3. Unfriend")
    print("4. Check if Two Users are Friends\n5. Show All Friends\n6. Exit")
    choice = input("What do you want to do? (Choose 1-6): ")
    if choice == "1":
        user1 = input("Your name: ")
        user2 = input("Friend's name: ")
        if user1 not in friends:friends[user1] = set()
        if user2 not in friends:friends[user2] = set()
        print(f"{user1} has sent a friend request to {user2}!")
    elif choice == "2":
        user1 = input("Your name: ")
        user2 = input("Who sent you the friend request? ")
        if user1 in friends and user2 in friends:
            friends[user1].add(user2)
            friends[user2].add(user1)
            print(f"{user1} and {user2} are now friends!")
        else:print("One of the users does not exist.")
    elif choice == "3":
        user1 = input("Your name: ")
        user2 = input("Who do you want to unfriend? ")
        if user1 in friends and user2 in friends:
            friends[user1].discard(user2)
            friends[user2].discard(user1)
            print(f"{user1} and {user2} are no longer friends.")
        else:print("One of the users does not exist.")
    elif choice == "4":
        user1 = input("Enter first name: ")
        user2 = input("Enter second name: ")
        if user1 in friends and user2 in friends and user2 in friends[user1]:
            print(f"{user1} and {user2} are friends.")
        else:print(f"{user1} and {user2} are not friends.")
    elif choice == "5":
        user = input("Enter your name: ")
        if user in friends:
            print(f"{user}'s friends: {friends}")         