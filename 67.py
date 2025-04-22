def check_palindrome():
    main_string = input("Enter the main string: ")
    pos1 = int(input("Enter position1: "))
    pos2 = int(input("Enter position2: "))
    substring = main_string[pos1:pos2+1]
    if substring == substring[::-1]: 
        print(f"'{substring}' is a palindrome")
    else:
        print(f"'{substring}' is NOT a palindrome")
check_palindrome()