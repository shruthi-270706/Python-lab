def menu():
    string=str(input("Enter the string: "))
    if string:
        print("1: No of characters:")
        print("2: No of words:")
        print("3: Reverse a string: ")
        print("4: Convert the string to uppercase: ")
        print("5: Replace the spaces with underscore: ")
        choice=str(input("Enter the chioce: "))
        if choice=='1':
            count=0
            for ch in string:
                count+=1
            print(count)
        elif choice=='2':
            count=0
            new_string=string.split(" ")
            for part in new_string:
                count+=1
            print(count)
        elif choice=='3':
            reverse=string[::-1]
            print(reverse)
        elif choice=='4':
            new_string=string.upper()
            print(new_string)
        else:
            result=string.replace(" ","_")
            print(result)
    else:
        print("It is not a string ")
menu()