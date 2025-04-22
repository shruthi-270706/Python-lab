source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
try:
    with open(source_file, "r") as sf:
        text = sf.read()
    print("\n1: Append\n2: Re-write")
    choice = int(input("Enter your choice (1 or 2): "))
    print("You chose:", choice)
    if choice == 1:
        with open(destination_file, "a") as df:
            df.write(text)
        print("Content appended.")
    elif choice == 2:
        with open(destination_file, "w") as df:
            df.write(text)
        print("Content rewritten.")
    else:print("Invalid choice.")
except FileNotFoundError: print("File not found")