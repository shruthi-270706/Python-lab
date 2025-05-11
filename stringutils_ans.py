from stringutils import string_manipulations as sm
name=input("Enter the string: ")
print("1:Reverse \n2:Palindrome ")
choice=int(input("Enter your choice: "))
if choice==1:
    reverse=sm.reverse_string(name)
    print(reverse)
elif choice==2:
    palindrome=sm.is_palindrome(name)
    print(palindrome)