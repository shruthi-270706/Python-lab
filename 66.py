def palindrome():
    number=input("Enter the numer: ")
    reverse_number=number[::-1]
    if (number==reverse_number): print("Palindrome")
    else : print("Not a palindrome")
palindrome()