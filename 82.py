def palindrome(string):
    new_string=string[::-1]
    if(string==new_string):return"palindrome"
    else: return"Not a palindrome"
string=str(input("Enter the string: "))
print(palindrome(string))