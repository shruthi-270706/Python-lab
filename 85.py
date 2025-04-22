def number(string):
    result=""
    for char in string:
        if char.isdigit():result+=char
    print(result)
string=input("Enter the string: ")
number(string)